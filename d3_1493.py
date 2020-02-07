import sys
sys.stdin = open('d3_1493_input.txt', 'r')

T = int(input())

# coordinates = [[[r_idx, c_idx] for r_idx in range(10)] for c_idx in range(10)]
# for row in coordinates:
#     print(row)
# layout = [[0 for _ in range(10)] for j in range(10)]
# number = 1
# for coordinate in coordinates[1]:
#     x, y = coordinate[0], coordinate[1]
#     if x == 0:
#         continue
#     if x == 1:
#         layout[x][y] = number
#         number += 1
#         continue
#     while x > 0:
#         layout[x][y] = number
#         x -= 1
#         y += 1
#         number += 1
# for row in layout:
#     print(row)

def find(number):
    n = 2
    while True:
        if number == 1:
            n = 1
            break
        elif n * (n-1) / 2 < number and (n + 1) * n / 2 >= number:
            break
        n += 1
    x_idx = n
    y_idx = 1
    total = n * (n-1) // 2
    while total != number and x_idx > 0:
        total += 1
        if total != number:
            x_idx -= 1
            y_idx += 1
    return [x_idx, y_idx]

for test_case in range(1, T+1):
    p, q = map(int, input().split())
    p_coordinates = find(p)
    q_coordinates = find(q)
    new_x, new_y = p_coordinates[0]+q_coordinates[0], p_coordinates[1]+q_coordinates[1]

    new_n = new_x + new_y - 1
    ans = new_n * (new_n - 1) // 2 + 1

    nx, ny = new_n, 1
    while nx != new_x:
        nx -= 1
        ny += 1
        ans += 1

    print('#{} {}'.format(test_case, ans))





























    # # p 좌표 찾기
    # p_coordinates = []
    # q_coordinates = []
    # for x_idx in range(len(layout)):
    #     for y_idx in range(len(layout[0])):
    #         if layout[x_idx][y_idx] == p:
    #             p_coordinates = [x_idx, y_idx]
    #         elif layout[x_idx][y_idx] == q:
    #             q_coordinates = [x_idx, y_idx]
    #         if p_coordinates and q_coordinates:
    #             break
    # ans_x, ans_y = p_coordinates[0]+q_coordinates[0], p_coordinates[1]+q_coordinates[1]
    # ans = layout[ans_x][ans_y]
    # print(ans)