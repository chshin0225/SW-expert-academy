def check_multiples(a):
    for idx in range(len(a)-1):
        if a[idx] == a[idx+1]:
            return True
    return False

for test_case in range(1, 3):
    length, string = input().split()
    length = int(length)
    result = string
    while check_multiples(result):
        for idx in range(len(result)-1):
            if result[idx] == result[idx+1]:
                result = result[:idx] + result[idx+2:]
                break
    print(result)