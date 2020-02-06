import sys
sys.stdin = open('1211_input.txt', 'r')

for test_case in range(10):
    test_case_no = int(input())
    layout = [[int(i) for i in input().split()] for _ in range(100)]

    # 모든 사다리 시작점들 구하기
    starting_points = [idx for idx in range(len(layout[0])) if layout[0][idx] == 1]
    # 각 시작점에서 출발하여 각각의 이동거리 구하기
    result = []
    for start_idx in starting_points:
        distance = 0
        current_idx = start_idx
        for row_idx in range(1, len(layout)):
            distance += 1
            # 현재 위치에서 양 옆으로 가로 사다리 있는지 확인
            # 왼쪽에 가로 사다리
            if layout[row_idx][current_idx-1] == 1 and current_idx - 1 >= 0:
                while layout[row_idx][current_idx-1] != 0 and current_idx - 1 >= 0:
                    current_idx -= 1
                    distance += 1
            # 오른쪽에 가로 사다리
            elif current_idx + 1 < len(layout[0]) and layout[row_idx][current_idx+1] == 1:
                while current_idx + 1 < len(layout[0]) and layout[row_idx][current_idx+1] != 0:
                    current_idx += 1
                    distance += 1
        # 이동거리를 결과 리스트에 시작점과 함께 첨부
        result.append((start_idx, distance))

    min_lane, min_distance = result[0][0], result[0][1]
    for lane, distance in result:
        if min_distance >= distance:
            min_lane = lane
            min_distance = distance

    print('#{} {}'.format(test_case_no, min_lane))




