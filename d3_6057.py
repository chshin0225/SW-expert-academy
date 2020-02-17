import sys
sys.stdin = open('d3_6057_input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    matrix = [[0 for _ in range(V+1)] for _ in range(V+1)]
    edges = [[int(i) for i in input().split()] for _ in range(E)]

    for edge in edges:
        u, v = edge
        matrix[u][v] = 1
        matrix[v][u] = 1

    triangle = 0
    for d1 in range(1, V+1):
        for d2 in range(1, V+1):
            if matrix[d1][d2] == 1:
                for d3 in range(1, V+1):
                    if matrix[d2][d3] == 1:
                        if matrix[d3][d1] == 1:
                            triangle += 1
    print('#{} {}'.format(test_case, triangle//6))





    # for point in range(1, V+1):
    #     stack = []
    #     visited = [0 for i in range(V + 1)]
    #     print('point', point)
    #     stack.append(point)
    #     visited[point] = 1
    #     while stack:
    #         dot = stack.pop()
    #         for i in range(1, V+1):
    #             if matrix[dot][i] == 1 and visited[i] == 0:
    #                 stack.append(i)
    #                 visited[i] = 1
    #                 print(i)
    #
    #
    #




