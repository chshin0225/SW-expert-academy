def my_max(a):
    max = a[0]
    for idx in range(1, len(a)):
        if a[idx] > max:
            max = a[idx]
    return max

def isdanjo(number):
    number_str = str(number)
    for idx in range(len(number_str)-1):
        if number_str[idx] > number_str[idx+1]:
            return False
    return True



T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = [int(i) for i in input().split()]
    result = []
    max_num = -1
    for idx in range(len(numbers) - 1):
        for next_idx in range(idx + 1, len(numbers)):
            product = numbers[idx] * numbers[next_idx]
            if isdanjo(product) and product > max_num:
                max_num = product
            else:
                continue

    print('#{} {}'.format(test_case, max_num))



# other solution

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = -1
    for i in range(len(arr)):
        for j in range(len(arr)):
            num = arr[i] * arr[j]
            if i < j and num > maxV:    # 문제에서 주어진 조건에 만족 할 때만 계산
                # 원본 숫자는 조작할 것이므로 copy를 만듦
                num_copy = num
                # 하나의 자리수에 올 수 있는 최대값이 9이므로 10으로 초기 세팅
                pre = 10
                isInc = True
                while num:
                    n = num % 10    # 1의 자리수 얻기
                    if pre < n:    # n이 이전 수보다 크면 -> 단조증가가 아님
                        isInc = False
                        break
                    num = num // 10
                    pre = n
                # 최대값 찾기
                if isInc:
                    if num_copy > maxV:
                        maxV = num_copy
    print('#{} {}'.format(test_case, maxV))

