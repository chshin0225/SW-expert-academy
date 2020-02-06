

T = int(input())

for test_case in range(1, T+1):
    D, A, B = map(int, input().split())
    count = B - A - 1
    for num in range(A, B+1):
        if str(D) not in str(num):
            count -= 1
        else:
            for divide in range(2, num):
                if num % divide == 0:
                    count -= 1
                    break
    print(count)

