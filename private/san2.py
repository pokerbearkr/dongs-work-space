import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def visualize_layout(layout, room_dimensions):
    fig, ax = plt.subplots(figsize=(8, 6))

    # 방 크기 설정
    ax.set_xlim(0, room_dimensions[0])
    ax.set_ylim(0, room_dimensions[1])

    # 가구 배치 시각화
    for furniture in layout.values():
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


# 예시 layout
example_layout = {
    "bed": {"position": (1.0, 1.0), "dimensions": (2.0, 1.6, 1.2), "name": "bed", "category": "bedroom"},
    "dresser": {"position": (1.5, 2.8), "dimensions": (1.2, 0.6, 0.9), "name": "dresser", "category": "bedroom"},
    "tv_stand": {"position": (3.5, 1.5), "dimensions": (1.8, 0.6, 0.5), "name": "tv_stand", "category": "living"},
    "sofa": {"position": (3.0, 2.5), "dimensions": (2.5, 1.5, 0.8), "name": "sofa", "category": "living"},
    "desk": {"position": (0.5, 3.0), "dimensions": (1.5, 0.8, 0.75), "name": "desk", "category": "study"},
    "chair": {"position": (0.8, 3.5), "dimensions": (0.6, 0.6, 0.9), "name": "chair", "category": "study"}
}

# 시각화
visualize_layout(example_layout, room_dimensions)