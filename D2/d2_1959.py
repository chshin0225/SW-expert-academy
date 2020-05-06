num_of_test_cases = int(input())

for i in range(1, num_of_test_cases + 1):
    case = [int(j) for j in input().split(' ')]
    n = case[0]
    m = case[1]
    a = [int(a) for a in input().split(' ')]
    b = [int(b) for b in input().split(' ')]
    results = []
    if n < m:
        for k in range(m - n + 1):
            result = 0
            for l in range(n):
                result += a[l] * b[l + k]
            results.append(result)
    else:
        for k in range(n - m + 1):
            result = 0
            for l in range(m):
                result += a[l + k] * b[l]
            results.append(result)
    print('#{} {}'.format(i, max(results)))
