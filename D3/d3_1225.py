import sys
sys.stdin = open('d3_1225_input.txt', 'r')

for test_case in range(10):
    test_case_no = int(input())
    nums = [int(i) for i in input().split()]
    cycle = [1, 2, 3, 4, 5]
    cycle_stage = 0
    while True:
        front_num = nums.pop(0)
        new_num = front_num - cycle[cycle_stage]
        if new_num > 0:
            nums.append(new_num)
            cycle_stage = (cycle_stage + 1) % 5
        else:
            nums.append(0)
            break

    print('#{}'.format(test_case_no), end=' ')
    for num in nums:
        print(num, end=' ')
    print()