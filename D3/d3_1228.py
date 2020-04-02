import sys
sys.stdin = open('d3_1228_input.txt', 'r')

for test_case in range(1, 11):
    # 원본 암호문 길이
    original_len = int(input())
    # 원본 암호문
    code = [int(i) for i in filter(None, input().split(' '))]
    # 명령문의 개수
    num_of_orders = int(input())
    # 명령문들을 받아서 보기 좋게 만들기
    orders = input()
    list_of_orders = orders.split(' I')
    for idx in range(1, num_of_orders):
        list_of_orders[idx] = 'I' + list_of_orders[idx]
    list_of_orders = [list(filter(None, order.split(' '))) for order in list_of_orders]
    
    for order in list_of_orders:
        position = int(order[1])
        num_of_added_nums = int(order[2])
        nums_to_add = list(map(int, order[3:]))
        code = code[:position] + nums_to_add + code[position:]
    
    result = code[:10]
    print('#{}'.format(test_case), end=' ')
    for r in result:
        print(r, end=' ')
    print()


