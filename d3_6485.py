import sys
sys.stdin = open('d3_6485_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    all_stops = [0] * 5000
    for _ in range(N):
        A, B = [int(i) for i in input().split()]
        busline_range = list(range(A, B+1))
        for bus_stop in busline_range:
            all_stops[bus_stop-1] += 1
    
    P = int(input())
    bus_stops = [int(input()) for _ in range(P)]

    result = []
    for i in bus_stops:
        result.append(all_stops[i-1])

    answer = '#{} '.format(test_case)
    for i in result:
        answer += str(i) + ' '
    print(answer[:-1])