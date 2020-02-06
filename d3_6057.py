import sys
sys.stdin = open('d3_6057_input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lines = [list(map(int, input().split())) for line in range(M)]
    result = 0
    for first_line in lines:
        triangle = set()
        first = first_line
        triangle.update(first)
        remaining_lines = [x for x in lines if x != first]
        for second_line in remaining_lines:
            second = second_line
            triangle.update(second)
            remaining_lines = [x for x in remaining_lines if x != second]
            for third_line in remaining_lines:
                third = third_line
                triangle.update(third)
                print(triangle)
                if len(triangle) == 3:
                    result += 1
    print('#{} {}'.format(test_case, int(result / 3)))

