from math import sqrt

# 가구 목록
furniture_list = [
    {"name": "bed", "dimensions": (2.0, 1.6, 1.2), "category": "bedroom"},
    {"name": "dresser", "dimensions": (1.2, 0.6, 0.9), "category": "bedroom"},
    {"name": "tv_stand", "dimensions": (1.8, 0.6, 0.5), "category": "living"},
    {"name": "sofa", "dimensions": (2.5, 1.5, 0.8), "category": "living"},
    {"name": "desk", "dimensions": (1.5, 0.8, 0.75), "category": "study"},
    {"name": "chair", "dimensions": (0.6, 0.6, 0.9), "category": "study"}
]

# 원룸 정보
room_dimensions = (5.0, 4.0, 2.5)  # length, width, height


def calculate_furniture_synergy(layout):
    """가구 간 시너지 점수 계산"""
    synergy_score = 0
    for f1 in layout.values():
        for f2 in layout.values():
            if f1 != f2:
                dx = abs(f1["position"][0] - f2["position"][0])
                dy = abs(f1["position"][1] - f2["position"][1])
                distance = sqrt(dx ** 2 + dy ** 2)

                if f1["category"] == "bedroom" and f2["category"] == "living":
                    synergy_score -= 1 / (distance + 1)  # 침대와 TV가 가까울수록 불리
                elif f1["category"] == "study" and f2["category"] == "study":
                    synergy_score += 1 / (1 + distance)  # 책상과 의자가 가까울수록 유리

    return synergy_score


def calculate_space_efficiency(layout):
    """공간 효율성 및 이동 거리 점수 계산"""
    total_area = room_dimensions[0] * room_dimensions[1]
    used_area = sum(f["dimensions"][0] * f["dimensions"][1] for f in layout.values())
    open_space_ratio = (total_area - used_area) / total_area

    center_x = room_dimensions[0] / 2
    center_y = room_dimensions[1] / 2
    avg_distance_from_center = sum(sqrt((f["position"][0] - center_x) ** 2 + (f["position"][1] - center_y) ** 2)
                                   for f in layout.values()) / len(layout)

    return open_space_ratio * 0.5 + (1 - avg_distance_from_center / max(room_dimensions[0], room_dimensions[1])) * 0.5


def objective_function(layout):
    """목적함수 계산"""
    furniture_synergy_score = calculate_furniture_synergy(layout)
    space_efficiency_score = calculate_space_efficiency(layout)

    total_score = furniture_synergy_score * 0.6 + space_efficiency_score * 0.4

    return total_score


# 예시 layout
example_layout = {
    "bed": {"position": (1.0, 1.0), "dimensions": (2.0, 1.6, 1.2), "category": "bedroom"},
    "dresser": {"position": (1.5, 2.8), "dimensions": (1.2, 0.6, 0.9), "category": "bedroom"},
    "tv_stand": {"position": (3.5, 1.5), "dimensions": (1.8, 0.6, 0.5), "category": "living"},
    "sofa": {"position": (3.0, 2.5), "dimensions": (2.5, 1.5, 0.8), "category": "living"},
    "desk": {"position": (0.5, 3.0), "dimensions": (1.5, 0.8, 0.75), "category": "study"},
    "chair": {"position": (0.8, 3.5), "dimensions": (0.6, 0.6, 0.9), "category": "study"}
}

# 예시 layout에 대한 목적함수 값 계산
score = objective_function(example_layout)
print(f"Objective function score: {score:.2f}")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def visualize_layout(layout, room_dimensions):
    fig, ax = plt.subplots(figsize=(8, 6))

    # 방 크기 설정
    ax.set_xlim(0, room_dimensions[0])
    ax.set_ylim(0, room_dimensions[1])

    # 가구 배치 시각화
    for furniture in layout:
        x, y = furniture["position"]
        width, length, height = furniture["dimensions"]

        # 가구 직사각형 패치 생성
        rect = Rectangle((x, y), width, length, linewidth=1, edgecolor='black', facecolor='lightgray')
        ax.add_patch(rect)

        # 가구 이름 표시
        ax.text(x + width / 2, y + length / 2, furniture["name"], ha='center', va='center', fontsize=8)

    # 축 설정
    ax.set_xlabel('Length (m)')
    ax.set_ylabel('Width (m)')
    ax.set_title('Furniture Layout')

    plt.show()

def get_furniture_info_from_user():
    furniture_list = []
    while True:
        name = input("가구의 이름을 입력하세요 (종료하려면 'exit' 입력): ")
        if name.lower() == 'exit':
            break

        try:
            length = float(input("가구의 길이(m)를 입력하세요: "))
            width = float(input("가구의 너비(m)를 입력하세요: "))
            height = float(input("가구의 높이(m)를 입력하세요: "))
            category = input("가구의 카테고리를 입력하세요: ")
            position_x = float(input("가구의 x 좌표를 입력하세요: "))
            position_y = float(input("가구의 y 좌표를 입력하세요: "))

            furniture_info = {
                "name": name,
                "dimensions": (length, width, height),
                "category": category,
                "position": (position_x, position_y)
            }
            furniture_list.append(furniture_info)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")

    return furniture_list

# 방 크기 입력
room_length = float(input("방의 길이(m)를 입력하세요: "))
room_width = float(input("방의 너비(m)를 입력하세요: "))
room_height = float(input("방의 높이(m)를 입력하세요: "))
room_dimensions = (room_length, room_width, room_height)

# 사용자로부터 가구 정보 입력 받기
user_furniture_list = get_furniture_info_from_user()

# 시각화
visualize_layout(user_furniture_list, room_dimensions)
