for test_case in range(1, 11):
    n = int(input())
    buildings = [int(i) for i in filter(None, input().split(' '))]
    layout = []
    # 하나의 리스트 안에 각 빌딩들의 높이를 1로 표현하기
    for height in buildings:
        building = [1] * height + [0] * (max(buildings) - height)
        layout.append(building)

    view_count = 0
    # layout 리스트 안에 1의 값들을 발견할 때마다 앞뒤 2건물의 같은 층이 0인지 확인하여 조망권을 가진 가구들을 판별
    for building_idx, building in enumerate(layout):
        for level_idx, level in enumerate(building):
            if level == 1:
                building_no = building_idx
                level_no = level_idx
                if layout[building_no + 1][level_no] == 0 and layout[building_no + 2][level_no] == 0 and \
                        layout[building_no - 1][level_no] == 0 and layout[building_no - 2][level_no] == 0:
                    view_count += 1

    print('#{} {}'.format(test_case, view_count))