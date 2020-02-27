import sys
sys.stdin = open('d4_1258_input.txt', 'r')


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    layout = [[int(i) for i in input().split()] for _ in range(N)]

    # 문제에 주어진 부분행렬 개수의 제한을 조건문으로 표현
    if N <= 10:
        max_matrix_count = 5
    elif N <= 40:
        max_matrix_count = 10
    elif N <= 80:
        max_matrix_count = 15
    elif N <= 100:
        max_matrix_count = 20

    visited = [[0 for _ in range(N)] for _ in range(N)]
    matrix_count = 0
    result = []
    for row in range(N):
        # 이미 존재할 수 있는 부분행렬의 개수만큼 찾았으면 더 이상 찾아봤자 없을 것이기 때문에 break
        if matrix_count == max_matrix_count:
            break
        for col in range(N):
            # 부분행렬의 왼쪽 위 시작점 찾기
            if layout[row][col] != 0 and visited[row][col] == 0:
                row_len = 0
                col_len = 0
                matrix_count += 1
                # 행 길이 재기
                for r in range(row, N):
                    if layout[r][col] == 0:
                        break
                    col_len += 1
                # 열 길이 재기
                for c in range(col, N):
                    if layout[row][c] == 0:
                        break
                    row_len += 1
                # 행과 열의 길이를 result에 넣기
                result.append([col_len, row_len])
                # 앞으로 탐색할때 이 부분행렬을 다시는 안 찾게 visited에 이 부분행렬의 좌표들을 다 1로 표시
                for r in range(row, row+col_len):
                    for c in range(col, col+row_len):
                        visited[r][c] = 1
    # 출력 형태에 맞게 sort
    result.sort(key=lambda x: (x[0]*x[1], x[0]))
    print('#{} {}'.format(test_case, matrix_count), end=' ')
    for x, y in result:
        print(x, y, end=' ')
    print()









