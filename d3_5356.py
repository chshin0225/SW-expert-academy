import sys
sys.stdin = open('d3_5356_input.txt', 'r')

def max_num(a):
    max = a[0]
    for i in range(1, len(a)):
        if a[i] > max:
            max = a[i]
    return max

T = int(input())

for test_case in range(1, T+1):
    n = 5
    strings = [[i for i in input()] for _ in range(n)]
    strings_len = [len(x) for x in strings]
    max_col = max_num(strings_len)
    result = []
    coordinates = [[x, y] for x in range(len(strings)) for y in range(len(strings[x]))]
    for col in range(max_col):
        col_result = []
        for coordinate in coordinates:
            if coordinate[1] == col:
                x = coordinate[0]
                y = coordinate[1]
                col_result.append(strings[x][y])
        result.append(col_result)
    result = [''.join(r) for r in result]
    result = ''.join(result)
    print('#{} {}'.format(test_case, result))