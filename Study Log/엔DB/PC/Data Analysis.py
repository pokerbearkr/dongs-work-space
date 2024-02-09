import geopandas as gpd
import contextily as ctx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, MultiPoint
from deap import base, creator, tools, algorithms
import random
import pandas as pd
from sqlalchemy import create_engine
from sklearn.ensemble import RandomForestRegressor

db_host = "localhost"
db_user = "root"
db_password = "autoset"
db_name = "project"

engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

query = '''
SELECT
    s.sigungu_code,
    COUNT(DISTINCT cs.station_id) as ChargingStationCount, 
    AVG(et.ALL_AADT) as average_total_traffic, 
    AVG(p.`total_population`) as average_total_population, 
    AVG(tcc.ALL_cost_CG) as average_total_congestion_cost, 
    AVG(va.area) as average_total_area,
    AVG(va.vehicle) as average_total_vehicle, 
    AVG(vm.ALL_VKT) as average_total_vehicle_mileage
FROM
    sigungu s
LEFT JOIN charging_station cs ON s.sigungu_code = cs.sigungu_code
LEFT JOIN estimated_traffic et ON s.sigungu_code = et.sigungu_code
LEFT JOIN population p ON s.sigungu_code = p.sigungu_code
LEFT JOIN traffic_congestion_cost tcc ON s.sigungu_code = tcc.sigungu_code
LEFT JOIN vehicle_area va ON s.sigungu_code = va.sigungu_code
LEFT JOIN vehicle_mileage vm ON s.sigungu_code = vm.sigungu_code
GROUP BY
    s.sigungu_code;
'''
df_1 = pd.read_sql(query, engine)
engine.dispose()

column_means = df_1.mean(axis=0)
df_1 = df_1.fillna(column_means)

X = df_1[['average_total_traffic', 'average_total_population', 'average_total_congestion_cost', 'average_total_area', 'average_total_vehicle', 'average_total_vehicle_mileage']]
y = df_1['ChargingStationCount']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

predictions = model.predict(X)

df_1['PredictedChargingStationCount'] = predictions
df_1['ShortageChargingStationCount'] = df_1['PredictedChargingStationCount'] - df_1['ChargingStationCount']

def geo_transform(DataFrame) :
    DataFrame['lat'] = DataFrame['lat'].astype(float)
    DataFrame['lon'] = DataFrame['lon'].astype(float)
    DataFrame['geometry'] = DataFrame.apply(lambda row : Point([row['lon'], row['lat']]), axis=1)
    DataFrame = gpd.GeoDataFrame(DataFrame, geometry='geometry')
    DataFrame.crs = 'epsg:4326'
    DataFrame = DataFrame.to_crs('epsg:5179')
    return DataFrame

df = pd.read_csv('전기차충전소_충전기_정보.csv', low_memory=False) # Dataframe 불러옴, 생략 가능
df_new = geo_transform(df)

gdf = gpd.read_file('sig.shp')
gdf.crs ='epsg:5179'
SIG_CD = '27200'
filtered_gdf = gdf[gdf['SIG_CD'] == SIG_CD]
ev_in_area = gpd.sjoin(df_new, filtered_gdf, how="inner", predicate="within")

df_1['sigungu_code'] = df_1['sigungu_code'].astype(int)
filtered_df = df_1[df_1['sigungu_code'] == int(SIG_CD)]
shortage_in_area = round(filtered_df['ShortageChargingStationCount'].iloc[0])

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox = base.Toolbox()

def create_location():
    minx, miny, maxx, maxy = filtered_gdf.total_bounds
    return [random.uniform(minx, maxx), random.uniform(miny, maxy)]

toolbox.register("attr_loc", create_location)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.attr_loc)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evaluate_location(individual):
    point = Point(individual)
    if not filtered_gdf.contains(point).any():
        return -1, 

    distances = df_new.geometry.distance(point)
    min_distance = distances.min()
    optimal_distance = 1000 # 적정 거리를 지정

    if min_distance < optimal_distance:
        return min_distance / optimal_distance,
    else:
        return 1 - (min_distance / optimal_distance),

toolbox.register("evaluate", evaluate_location)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

def run_genetic_algorithm(shortage_count, current_best_individuals):
    population = toolbox.population(n=50)
    ngen = 10 # 세대 진행 수의 조절이 가능
    cxpb, mutpb = 0.5, 0.2

    for ind in current_best_individuals:
        population.append(creator.Individual(ind))

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    final_pop, logbook = algorithms.eaSimple(population, toolbox, cxpb, mutpb, ngen, stats=stats, verbose=True)
    return tools.selBest(final_pop, shortage_count)

best_individuals = []

for _ in range(shortage_in_area): # For문 사용
    new_individuals = run_genetic_algorithm(1, best_individuals)
    best_individuals.extend(new_individuals)
    best_individuals = list(set(map(tuple, best_individuals)))

print(best_individuals) # 최종 점검 확인용

added_label = False

fig, ax = plt.subplots(figsize=(10,10))
filtered_gdf.plot(ax=ax, edgecolor='black', color='none')
ev_in_area.plot(ax=ax, marker='o', color='red', markersize=5, label='Previous')

for individual in best_individuals:
    ax.scatter(individual[0], individual[1], marker='*', color='blue', s=100, label='Added' if not added_label else '')
    added_label = True

ctx.add_basemap(ax, crs=filtered_gdf.crs)
plt.legend()
plt.show()