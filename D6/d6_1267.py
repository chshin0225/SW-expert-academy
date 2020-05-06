import sys
sys.stdin = open('d6_1267_input.txt', 'r')

def dfs(s):
    pass

for test_case in range(1, 6):
    V, E = map(int, input().split())
    arr = input().split()
    edges = [[int(arr[i]), int(arr[i+1])] for i in range(0, len(arr), 2)]

    matrix = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for e1, e2 in edges:
        matrix[e1][e2] = 1

    matrix_t = [[matrix[i][j] for i in range(V+1)] for j in range(V+1)]

    possible_starting_points = [n for n in range(1, V+1) if matrix[n].count(1) and not matrix_t[n].count(1)]

    for s in possible_starting_points:
        dfs(s)


    # for row in matrix:
    #     print(row)
    #
    # for row in matrix_t:
    #     print(row)

    print('#{}'.format(test_case))

