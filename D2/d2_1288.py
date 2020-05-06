num_of_test_cases = int(input())

for i in range(1, num_of_test_cases + 1):
    num = int(input())
    numbers_that_appeared = set([int(i) for i in str(num)])
    count = 1
    result = num
    while len(numbers_that_appeared) < 10:
        result += num
        count += 1
        numbers_that_appeared.update(set([int(j) for j in str(result)]))
    print('#{} {}'.format(i, num * count))
