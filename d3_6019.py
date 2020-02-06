import sys
sys.stdin = open('d3_6012_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    D, A, B, F = [float(i) for i in input().split(' ')]
    time = D / (A + B)
    F_distance = time * F
    print('#{} {}'.format(test_case, F_distance))
