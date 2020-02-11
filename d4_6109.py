import sys
sys.stdin = open('d4_6109_input.txt', 'r')

# 왼쪽으로 한번 push
def push(layout):
    for row in range(len(layout)):
        for col in range(1, len(layout[0])):
            if layout[row][col-1] == 0 and layout[row][col] != 0:
                layout[row][col-1], layout[row][col] = layout[row][col], 0
    return layout

# 반시계 방향으로 90도 회전
def turn(layout):
    layout = [[layout[j][i] for j in range(len(layout))] for i in range(len(layout[0]) - 1, -1, -1)]
    return layout

T = int(input())

for test_case in range(1, T+1):
    N, d = input().split()
    N = int(N)
    layout = [[int(i) for i in input().split()] for _ in range(N)]

    if d == 'left':
        times = 0
    elif d == 'up':
        times = 1
    elif d == 'right':
        times = 2
    # d == 'down'
    else:
        times = 3

    for _ in range(times):
        layout = turn(layout)

    for _ in range(N):
        layout = push(layout)

    for row in range(len(layout)):
            for col in range(len(layout)-1):
                if layout[row][col] == layout[row][col+1] and layout[row][col] != 0 and layout[row][col+1] != 0:
                    layout[row][col] += layout[row][col+1]
                    layout[row][col+1] = 0

    for _ in range(N):
        layout = push(layout)

    if d == 'up':
        times = 3
    elif d == 'right':
        times = 2
    elif d == 'down':
        times = 1
    else:
        times = 0

    for _ in range(times):
        layout = turn(layout)

    print('#{}'.format(test_case))
    for row in layout:
        for num in row:
            print(num, end=' ')
        print()

