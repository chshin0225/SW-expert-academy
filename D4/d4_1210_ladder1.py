import sys
sys.stdin = open('d4_1210_input.txt', 'r')

for test_case in range(10):
    test_case_no = int(input())
    N = 100
    ladder = [[int(i) for i in input().split()] for _ in range(N)]
    r_ladder = [ladder[i] for i in range(N-1, -1, -1)]
    starting_point = col = r_ladder[0].index(2)
    row = 0
    while True:
        if row == 99:
            break
        row += 1
        if col+1 < N and r_ladder[row][col+1] == 1:
            while col+1 < N and r_ladder[row][col+1] == 1:
                col += 1
        elif col-1 >= 0 and r_ladder[row][col-1] == 1:
            while col-1 >= 0 and r_ladder[row][col-1] == 1:
                col -= 1
    result = col
    print('#{} {}'.format(test_case_no, result))


# teacher's solution

def find(sr, sc):
    # 오, 왼, 위
    dr = [0, 0, -1]
    dc = [1, -1, 0]

    while True:
        for k in range(3):
            nr = sr + dr[k]
            nc = sc + dc[k]
            if nr >= 0 and nr < 100 and nc >= 0 and nc < 100:
                if ladder[nr][nc] == 1:
                    break
        if nr == 0:
            return nc
        # 지나온 길은 다시 안 올거니까 아예 0으로 만들어 버림
        ladder[nr][nc] = 0
        # 현재 위치 갱신
        sr = nr
        sc = nc



for tc in range(10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    start = 0
    for i in range(100):
        if ladder[99][i] == 2:
            start = i
    print('#{} {}'.format(t, find(99, start)))



