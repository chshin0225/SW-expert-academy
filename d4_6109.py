import sys
sys.stdin = open('d4_6109_input.txt', 'r')

def push(layout, d):
    for row in range(len(layout)):
        for col in range(1, len(layout[0])):
            if layout[row][col-1] == 0 and layout[row][col] != 0:
                layout[row][col-1], layout[row][col] = layout[row][col], 0

def turn(layout):
    for col in range(len(layout[0])):
        for row in range(len(layout)):
            print([col, row])

T = int(input())

for test_case in range(1, T+1):
    N, d = input().split()
    N = int(N)
    layout = [[int(i) for i in input().split()] for _ in range(N)]



# # 숫자들을 한쪽으로 밀어주는 함수 정의
# def push(layout, d):
#     if d == 'up':
#         for col in range(len(layout[0])):
#             for row in range(1, len(layout)):
#                 if layout[row-1][col] == 0:
#                     layout[row-1][col], layout[row][col] = layout[row][col], 0
#     elif d == 'right':
#         for row in range(len(layout)):
#             for col in range(len(layout[0])-1):
#                 if layout[row][col+1] == 0:
#                     layout[row][col], layout[row][col+1] = 0, layout[row][col]
#     elif d == 'down':
#         for col in range(len(layout[0])):
#             for row in range(len(layout)-1):
#                 if layout[row+1][col] == 0:
#                     layout[row][col], layout[row+1][col] = 0, layout[row][col]
#     # d == 'left'
#     else:
#         for row in range(len(layout)):
#             for col in range(1, len(layout[0])):
#                 if layout[row][col-1] == 0:
#                     layout[row][col-1], layout[row][col] = layout[row][col], 0
#     return layout
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     N, d = input().split()
#     N = int(N)
#     layout = [[int(i) for i in input().split()] for _ in range(N)]
#
#     # for row in layout:
#     #     print(row)
#     # print('============================')
#
#     for _ in range(N):
#         layout = push(layout, d)
#
#     # 명령어가 up인 경우
#     if d == 'up':
#         for col in range(len(layout[0])):
#             for row in range(len(layout)-1):
#                 if layout[row][col] == layout[row+1][col] and layout[row][col] != 0 and layout[row+1][col] != 0:
#                     layout[row][col] += layout[row+1][col]
#                     layout[row+1][col] = 0
#                     layout = push(layout, d)
#
#     # 명령어가 right인 경우
#     elif d == 'right':
#         for row in range(len(layout)):
#             for col in range(1, len(layout[0])):
#                 if layout[row][col-1] == layout[row][col] and layout[row][col-1] != 0 and layout[row][col] != 0:
#                     layout[row][col] += layout[row][col-1]
#                     layout[row][col-1] = 0
#                     layout = push(layout, d)
#
#
#     # 명령어가 down인 경우
#     elif d == 'down':
#         for col in range(len(layout[0])):
#             for row in range(1, len(layout)):
#                 if layout[row-1][col] == layout[row][col] and layout[row-1][col] != 0 and layout[row][col] != 0:
#                     layout[row][col] += layout[row-1][col]
#                     layout[row-1][col] = 0
#                     layout = push(layout, d)
#
#     # 명령어가 left
#     else:
#         for row in range(len(layout)):
#             for col in range(len(layout)-1):
#                 if layout[row][col] == layout[row][col+1] and layout[row][col] != 0 and layout[row][col+1] != 0:
#                     layout[row][col] += layout[row][col+1]
#                     layout[row][col+1] = 0
#                     layout = push(layout, d)
#     # for row in layout:
#     #     print(row)
#
#     print('#{}'.format(test_case))
#     for row in layout:
#         for num in row:
#             print(num, end=' ')
#         print()




# # 숫자들을 한쪽으로 밀어주는 함수 정의
# def push(layout, d):
#     if d == 'up':
#         for col in range(len(layout[0])):
#             for row in range(1, len(layout)):
#                 if layout[row - 1][col] == 0 and layout[row][col] != 0:
#                     layout[row - 1][col], layout[row][col] = layout[row][col], 0
#     elif d == 'right':
#         for row in range(len(layout)):
#             for col in range(len(layout[0]) - 1, 0, -1):
#                 if layout[row][col] == 0 and layout[row][col - 1] != 0:
#                     layout[row][col], layout[row][col - 1] = layout[row][col - 1], 0
#     elif d == 'down':
#         for col in range(len(layout[0])):
#             for row in range(len(layout) - 1, 0, -1):
#                 if layout[row][col] == 0 and layout[row - 1][col] != 0:
#                     layout[row][col], layout[row - 1][col] = layout[row - 1][col], 0
#     # d == 'left'
#     else:
#         for row in range(len(layout)):
#             for col in range(1, len(layout[0])):
#                 if layout[row][col - 1] == 0 and layout[row][col] != 0:
#                     layout[row][col - 1], layout[row][col] = layout[row][col], 0
#     return layout
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, d = filter(None, input().split())
#     N = int(N)
#     layout = [[int(i) for i in filter(None, input().split())] for _ in range(N)]
#
#     for _ in range(N):
#         layout = push(layout, d)
#
#     # 명령어가 up인 경우
#     if d == 'up':
#         for col in range(len(layout[0])):
#             for row in range(len(layout) - 1):
#                 if layout[row][col] == layout[row + 1][col] and layout[row][col] != 0 and layout[row + 1][col] != 0:
#                     layout[row][col] += layout[row + 1][col]
#                     layout[row + 1][col] = 0
#     # 명령어가 right인 경우
#     elif d == 'right':
#         for row in range(len(layout)):
#             for col in range(len(layout[0]) - 1, 0, -1):
#                 if layout[row][col] == layout[row][col - 1] and layout[row][col - 1] != 0 and layout[row][col] != 0:
#                     layout[row][col] += layout[row][col - 1]
#                     layout[row][col - 1] = 0
#                     # 명령어가 down인 경우
#         for col in range(len(layout[0])):
#             for row in range(len(layout) - 1, 0, -1):
#                 if layout[row][col] == layout[row - 1][col] and layout[row - 1][col] != 0 and layout[row][col] != 0:
#                     layout[row][col] += layout[row - 1][col]
#                     layout[row - 1][col] = 0
#     # 명령어가 left
#     else:
#         for row in range(len(layout)):
#             for col in range(len(layout[0]) - 1):
#                 if layout[row][col] == layout[row][col + 1] and layout[row][col] != 0 and layout[row][col + 1] != 0:
#                     layout[row][col] += layout[row][col + 1]
#                     layout[row][col + 1] = 0
#
#     for _ in range(N):
#         layout = push(layout, d)
#
#     print('#{}'.format(test_case))
#     for row in layout:
#         for num in row:
#             print(num, end=' ')
#         print()