# 20 = 2 * 2 * 5
num_of_test_cases = int(input('number of test case?'))

for i in range(1, num_of_test_cases+1):
    num = int(input('test case?'))
    prime_nums = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    while num > 1:
        for prime_num in prime_nums:
            if num % prime_num == 0:
                prime_nums[prime_num] += 1
                num = num // prime_num
    result = '#{} '.format(i)
    for k, v in prime_nums.items():
        result += '{} '.format(v)
    print(result)



