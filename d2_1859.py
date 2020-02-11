T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    prices = [int(i) for i in input().split()]

    profit = 0
    stock = 0

    for day in prices:
        