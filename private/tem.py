import matplotlib.pyplot as plt
import numpy as np

def visualize_furniture_placement(room_area, furniture_positions):
    # 방의 면적과 가구 위치 리스트를 입력받습니다.
    # room_area: 방의 면적 (제곱 미터)
    # furniture_positions: 가구 위치 리스트 (제곱 미터)

    # 정사각형 방을 그립니다.
    plt.figure(figsize=(6, 6))
    plt.plot([0, np.sqrt(room_area)], [0, 0], 'k-')
    plt.plot([0, 0], [0, np.sqrt(room_area)], 'k-')
    plt.plot([0, np.sqrt(room_area)], [np.sqrt(room_area), np.sqrt(room_area)], 'k-')
    plt.plot([np.sqrt(room_area), np.sqrt(room_area)], [0, np.sqrt(room_area)], 'k-')

    # 가구 위치를 표시합니다.
    for pos in furniture_positions:
        plt.scatter(pos, pos, color='red', marker='o')

    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.title('Furniture Placement')
    plt.grid(True)
    plt.show()

# 사용 예시
room_area = 25  # 방의 면적 (제곱 미터)
furniture_positions = [4, 8, 12]  # 가구 위치 리스트 (제곱 미터)

visualize_furniture_placement(room_area, furniture_positions)
