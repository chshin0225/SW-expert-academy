num_of_test_cases = int(input())

for i in range(1, num_of_test_cases+1):
    string = input()
    for j in range(1, 10):
        if string[:j] == string[j:len(string[:j])*2]:
            result = j
            break
    print('#{} {}'.format(i, result))