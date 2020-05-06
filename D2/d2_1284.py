num_of_test_cases = int(input())

for i in range(1, num_of_test_cases + 1):
    nums = input().split(' ')
    P = int(nums[0])
    Q = int(nums[1])
    R = int(nums[2])
    S = int(nums[3])
    W = int(nums[4])
    fee_a = W * P
    if W <= R:
        fee_b = Q
    else:
        fee_b = Q + S * (W - R)
    if fee_a > fee_b:
        result = fee_b
    else:
        result = fee_a
    print('#{} {}'.format(i, result))

