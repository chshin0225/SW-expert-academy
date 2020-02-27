import sys
sys.stdin = open('d4_1258_input.txt', 'r')

def sort_matrix(a):
    def size(arr):
        return arr[0] * arr[1]
    # 크기대로 bubblesort
    for i in range(len(a)-1, -1, -1):
        for j in range(i):
            if size(a[j]) > size(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    # 같은 크기는 행이 작은 순대로 sort
    for k in range(len(a)-1):
        if size(a[k]) == size(a[k+1]):
            if a[k][0] > a[k+1][0]:
                a[k], a[k + 1] = a[k + 1], a[k]
    return a

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

    visited = []
    matrix_count = 0
    result = []
    for row in range(N):
        for col in range(N):
            # 이미 존재할 수 있는 부분행렬의 개수만큼 찾았으면 더 이상 찾아봤자 없을 것이기 때문에 break
            if matrix_count == max_matrix_count:
                break
            # 부분행렬의 왼쪽 위 시작점 찾
            if layout[row][col] != 0 and [row, col] not in visited:
                row_len = 1
                col_len = 1
                cur_row = row
                cur_col = col
                matrix_count += 1
                # 행 길이 재기
                while 0 <= cur_row+1 < N and layout[cur_row+1][col] != 0:
                    cur_row += 1
                    col_len += 1
                # 열 길이 재기
                while 0 <= cur_col+1 < N and layout[row][cur_col+1] != 0:
                    cur_col += 1
                    row_len += 1
                # 행과 열의 길이를 result에 넣기
                result.append([col_len, row_len])
                # 앞으로 탐색할때 이 부분행렬을 다시는 안 찾게 visited에 이 부분행렬의 좌표들을 다 append
                for r in range(row, cur_row+1):
                    for c in range(col, cur_col+1):
                        visited.append([r, c])
    # 출력 형태에 맞게 sort
    result = sort_matrix(result)
    print('#{} {}'.format(test_case, matrix_count), end=' ')
    for r in result:
        for s in r:
            print(s, end=' ')
    print()










