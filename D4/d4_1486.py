import sys
sys.stdin = open('d4_1486_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, B = map(int, input().split())
    heights = [int(i) for i in input().split()]

    diff = sum(heights) - B
    for i in range(1 << N):
        total_sum = 0
        for j in range(N):
            if i & (1 << j):
                total_sum += heights[j]
                if total_sum >= B:
                    if total_sum - B < diff:
                        diff = total_sum - B

    print('#{} {}'.format(test_case, diff))



