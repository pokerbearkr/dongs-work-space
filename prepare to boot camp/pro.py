import math
from ortools.linear_solver import pywraplp

# 데이터 입력
num_furniture = 4
areas = [10, 8, 6, 5]
closeness_weights = [[0, 3, 1, 2], [3, 0, 2, 1], [1, 2, 0, 3], [2, 1, 3, 0]]
shape_ratio_weight = 0.5

# 최적화 모델 생성
solver = pywraplp.Solver.CreateSolver('SCIP')

# 변수 정의
x_coords = [solver.NumVar(0, 100, 'x%d' % i) for i in range(num_furniture)]
y_coords = [solver.NumVar(0, 100, 'y%d' % i) for i in range(num_furniture)]
width = solver.NumVar(0, 100, 'width')
height = solver.NumVar(0, 100, 'height')

# 제약조건 정의
for i in range(num_furniture):
    solver.Add(x_coords[i] + areas[i] <= width)
    solver.Add(y_coords[i] + areas[i] <= height)

# 유클리드 거리 계산을 위한 제약식 정의
distances = {}
for i in range(num_furniture):
    for j in range(i):
        distances[(i, j)] = solver.NumVar(0, solver.infinity(), '')
        constraint = solver.Constraint(-solver.infinity(), solver.infinity())
        constraint.SetCoefficient(distances[(i, j)], 1)
        constraint.SetCoefficient(x_coords[i], -1)
        constraint.SetCoefficient(x_coords[j], 1)
        constraint.SetCoefficient(y_coords[i], -1)
        constraint.SetCoefficient(y_coords[j], 1)
        dx = x_coords[i] - x_coords[j]
        dy = y_coords[i] - y_coords[j]
        constraint.SetBounds(math.sqrt(solver.Sum([dx**2, dy**2])), solver.infinity())

# 목적함수 정의
total_distance = solver.Sum(closeness_weights[i][j] * distances[(i, j)]
                            for i in range(num_furniture) for j in range(i))
shape_ratio = width * height / solver.Sum(areas)
objective = solver.Objective()
objective.SetMinimization(total_distance + shape_ratio_weight * (1 / shape_ratio))

# 최적화 실행
status = solver.Solve()

# 결과 출력
if status == pywraplp.Solver.OPTIMAL:
    print(f'Optimal value: {solver.Objective().Value()}')
    for i in range(num_furniture):
        print(f'Furniture {i}: ({x_coords[i].solution_value()}, {y_coords[i].solution_value()})')
    print(f'Width: {width.solution_value()}, Height: {height.solution_value()}')
else:
    print('No optimal solution found.')