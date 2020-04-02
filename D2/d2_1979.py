num_of_test_cases = int(input())

for i in range(1, num_of_test_cases + 1):
    nums = [int(j) for j in input().split(' ')]
    n = nums[0]
    k = nums[1]
    match_count = 0

    hor_puzzle = []
    for k in range(n):
        line = [0] + [int(l) for l in filter(None, input().split(' '))] + [0]
        hor_puzzle.append(line)
    print(hor_puzzle)
    for hor_line in hor_puzzle:
        for scan in range(n - k + 1):
            if hor_line[scan:scan + k + 2] == [0] + [1] * k + [0]:
                match_count += 1

    ver_puzzle = []
    for m in range(1, n+1):
        line2 = [0] + [hor_line[m] for hor_line in hor_puzzle] + [0]
        ver_puzzle.append(line2)
    print(ver_puzzle)
    for ver_line in ver_puzzle:
        for scan2 in range(n - k + 1):
            if ver_line[scan2:scan2 + k + 2] == [0] + [1] * k + [0]:
                match_count += 1

    print('#{} {}'.format(i, match_count))
