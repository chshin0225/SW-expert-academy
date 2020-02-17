T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    edges = [[int(i) for i in input().split()] for _ in range(M)]
    matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    # 인접행렬
    for edge in edges:
        u, v = edge[0], edge[1]
        matrix[u][v] = 1
        matrix[v][u] = 1
    max_route = 0
    for dot in range(1, N + 1):
        route = []
        route.append(dot)
        for i in range(len(matrix[dot])):
            if matrix[dot][i] == 1 and i not in route:
                route.append(i)
        print(route)
        if len(route) > max_route:
            max_route = len(route)

    print('#{} {}'.format(test_case, max_route))


