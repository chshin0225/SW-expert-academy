
T = int(input())

for test_case in range(1, T + 1):
    A, B, C = [int(i) for i in filter(None, input().split())]
    max_count_a = C // A
    max_count_b = C // B

    result = max_count_a if max_count_a > max_count_b else max_count_b
    print('#{} {}'.format(test_case, result))