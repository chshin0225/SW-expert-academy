import sys
sys.stdin = open('1226_미로1_input.txt', 'r')

for test_case in range(10):
    test_case_no = int(input())
    N = 16
    maze = [[int(i) for i in input()] for _ in range(N)]

    result = 0
    visited = [(1, 1)]
    stack = [(1, 1)]
    while len(stack) != 0:
        next = stack.pop()
        x, y = next[0], next[1]
        # 위, 오, 아, 왼
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            if maze[x+dx[i]][y+dy[i]] == 3:
                result = 1
                break
            if maze[x+dx[i]][y+dy[i]] == 0 and (x+dx[i], y+dy[i]) not in visited:
                stack.append((x+dx[i], y+dy[i]))
                visited.append((x+dx[i], y+dy[i]))
        if result == 1:
            break
    print('#{} {}'.format(test_case_no, result))



