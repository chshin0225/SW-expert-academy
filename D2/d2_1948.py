num_of_test_cases = int(input())

days_in_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for i in range(1, num_of_test_cases+1):
    dates = [int(i) for i in input().split(' ')]
    first_date = dates[:2]
    second_date = dates[2:]
    if first_date[0] == second_date[0]:
        result = second_date[1] - first_date[1] + 1
    else:
        first_month_remaining_days = days_in_year[first_date[0]] - first_date[1] + 1
        second_month_preceding_days = second_date[1]
        inbetween_months_days = 0
        for month in range(first_date[0]+1, second_date[0]):
        	inbetween_months_days += days_in_year[month]
        result = first_month_remaining_days + second_month_preceding_days + inbetween_months_days
    print('#{} {}'.format(i, result))