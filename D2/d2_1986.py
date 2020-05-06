num_of_test_cases = int(input('number of test cases?'))

for i in range(1, num_of_test_cases+1):
    num = int(input('number?'))
    result = 0
    for j in range(1, num+1):
        if j % 2:
            result += j
        else:
            result -=j
    print('#{} {}'.format(i, result))