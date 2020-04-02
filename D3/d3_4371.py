T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    happy_days = [int(input()) for _ in range(N)]

    boats = N - 1
    remaining_days = happy_days
    while len(remaining_days) > 1:
        happy_day = remaining_days[1]
        diff = happy_day - 1
        same_boat = [happy_day]
        for i in range(2, len(remaining_days)):
            if (remaining_days[i] - 1) % diff == 0:
                boats -= 1
                same_boat.append(remaining_days[i])
        remaining_days = [day for day in remaining_days if day not in same_boat]

    print('#{} {}'.format(test_case, boats))