import sys
sys.stdin = open('d3_5789_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    result = [0] * N
    for times in range(1, Q+1):
        L, R = map(int, input().split())
        result = result[:L-1] + [times] * (R - L +1) + result[R:]
    print(result)