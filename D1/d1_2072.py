num_of_test_cases = input()

for i in range(1, num_of_test_cases + 1):
    string = input()
    nums = list(map(lambda x: int(x), string.split(' ')))
    print(nums)
    print('#{} {}'.format(i, sum(nums)))