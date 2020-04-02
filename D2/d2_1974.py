import sys
sys.stdin = open('d2_1974_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = 9
    puzzle = [[i for i in input().split()] for _ in range(N)]
    result = 1
    # 가로
    for row in puzzle:
        if len(row) != len(set(row)):
            result = 0
    # 세로
    for col_idx in range(N):
        hor_line = [puzzle[row_idx][col_idx] for row_idx in range(N)]
        if len(hor_line) != len(set(hor_line)):
            result = 0

    # 네모
    for r_idx in range(0, N, 3):
        for c_idx in range(0, N, 3):
            square = [puzzle[r][c] for r in range(r_idx, r_idx+3) for c in range(c_idx, c_idx+3)]
            if len(square) != len(set(square)):
                result = 0

    print('#{} {}'.format(test_case, result))


