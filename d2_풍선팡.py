def petals(balloons, r_idx, c_idx):
    total = balloons[r_idx][c_idx]
    # print('current', r_idx, c_idx)
    # 위, 오, 아, 왼
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    i = 0
    j = 1
    while j < (balloons[r_idx][c_idx] + 1):
        if 0 <= (c_idx + dy[i] * j) < len(balloons[0]) and 0 <= (r_idx + dx[i] * j) < len(balloons):
            # print(r_idx + dx[i] * j, c_idx + dy[i] * j)
            total += balloons[r_idx + dx[i] * j][c_idx + dy[i] * j]
        if (i + 1) % 4 == 0:
            j += 1
            i = 0
        else:
            i += 1
    return total


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    balloons = [[int(i) for i in input().split()] for _ in range(N)]
    max_petals = 0
    for r_idx in range(len(balloons)):
        for c_idx in range(len(balloons[0])):
            # petals(balloons, r_idx, c_idx)
            if max_petals < petals(balloons, r_idx, c_idx):
                max_petals = petals(balloons, r_idx, c_idx)
    print('#{} {}'.format(test_case, max_petals))