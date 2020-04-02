import sys
sys.stdin = open('d3_1220_input.txt', 'r')

for test_case in range(1, 11):
    N = int(input())
    table = [[int(i) for i in input().split()] for _ in range(N)]
    table = [[table[a][b] for a in range(N)] for b in range(N)]

    # 왼쪽에 N극, 오른쪽에 S극
    # 1: N  2: S
    result = 0
    for row in table:
        stack = []
        for m in row:
            if m == 1:
                stack.append(m)
            elif m == 2:
                if not stack:
                    continue
                stack = []
                result += 1
    print('#{} {}'.format(test_case, result))

