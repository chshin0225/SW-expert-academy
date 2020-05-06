import sys

sys.stdin = open('d3_5215_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, L = map(int, input().split())
    info = [[int(i) for i in filter(None, input().split())] for _ in range(N)]

    max_score = 0
    for i in range(1 << N):
        score = 0
        calories = 0
        for j in range(N):
            if i & (1 << j):
                score += info[j][0]
                calories += info[j][1]
                if calories > L:
                    break
        if calories > L:
            continue
        elif score > max_score:
            max_score = score

    print('#{} {}'.format(test_case, max_score))


