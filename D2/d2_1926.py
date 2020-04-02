N = int(input())

result = ''
for num in range(1, N+1):
    if '3' not in str(num) and '6' not in str(num) and '9' not in str(num):
        result += str(num) + ' '
    else:
        claps = 0
        for n in str(num):
            if n in ['3', '6', '9']:
                claps += 1
        result += '-' * claps + ' '

    print(result)
                