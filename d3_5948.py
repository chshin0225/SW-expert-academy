def sorting(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

T = int(input())

for test_case in range(1, T+1):
    nums = [int(i) for i in input().split()]
    sums = []
    for first_num in nums:
        first = first_num
        remaining_nums = [x for x in nums if x != first]
        for second_num in remaining_nums:
            second = second_num
            remaining_nums = [x for x in remaining_nums if x != second]
            for third_num in remaining_nums:
                third = third_num
                sums.append(first+second+third)
    sums = list(set(sorting(sums)))
    result = sums[-5]
    print('#{} {}'.format(test_case, result))