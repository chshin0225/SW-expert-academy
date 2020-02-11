import sys
sys.stdin = open('d3_6057_input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lines = [list(map(int, input().split())) for line in range(M)]
    for dot in range(1, N+1):



    # print('#{} {}'.format(test_case, count))
