# import sys
# sys.stdin = open('d3_2806_input.txt', 'r')

# 퀸을 하나 놓을 때, 이 위치에 놓으면 다른 퀸들을 죽이는지 알려주는 함수 정의
def queen(row, col, N):
    global cols
    global cnt

    def possible(cols, row, col):
        # 대각선 탐색
        if col not in cols:
            for r in range(1, row):
                if abs(r - row) == abs(cols[r] - col):
                    return False
        # 세로 탐색
        elif col in cols:
            return False
        return True

    if row == N+1:
        if 0 not in cols[1:]:
            print('answer', cols)
            cnt += 1
        return
    while col < N + 1:
        if possible(cols, row, col):
            cols[row] = col
            print(cols)
            queen(row+1, 1, N)
        col += 1
    # print(cols)
    # 놓을 수 없는 경우
    if cols[row] == 0 and row-1 > 0:
        newcol = cols[row-1]+1
        cols[row-1] = 0
        queen(row-1, newcol, N)









T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cols = [0] * (N+1)    # 1~N행: 몇번째 열에 체스가 놓여있는지 보여줌
    cnt = 0
    queen(1, 1, N)
    print('#{} {}'.format(test_case, cnt))





















# def check(layout):
#     def kill_queen(layout, row_idx, col_idx):
#         N = len(layout)
#         c = 0
#         while c < N:
#             if layout[row_idx][c] == 1 and c != col_idx:
#                 return True
#             c += 1
#         r = 0
#         while r < N:
#             if layout[r][col_idx] == 1 and r != row_idx:
#                 return True
#             r += 1
#
#         if row_idx > col_idx:
#             r, c = row_idx - col_idx, 0
#         else:
#             r, c = 0, col_idx - row_idx
#         while r < N and c < N:
#             if layout[r][c] == 1 and r != row_idx and c != col_idx:
#                 return True
#             r += 1
#             c += 1
#
#         if row_idx > col_idx:
#             r, c = row_idx + col_idx, 0
#         else:
#             r, c = 0, col_idx + row_idx
#         while r < N and c < N:
#             if layout[r][c] == 1 and r != row_idx and c != col_idx:
#                 return True
#             r -= 1
#             c += 1
#         return False
#     for row_idx in range(len(layout)):
#         for col_idx in range(len(layout[0])):
#             if layout[row_idx][col_idx] == 1:
#                 if kill_queen(layout, row_idx, col_idx):
#                     return False
#     return True
#
# def count_queen(layout):
#     queens = 0
#     for row in layout:
#         queens += row.count(1)
#     return queens
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     N = int(input())
#     board = [[0 for i in range(N)] for j in range(N)]
#
#     count = 0
#     for idx in range(N):
#         board[0][idx] = 1
#         for row_idx in range(1, N):
#             for col_idx in range(N):
#                 board[row_idx][col_idx] = 1
#                 if not check(board):
#                     board[row_idx][col_idx] = 0
#                     continue
#                 else:
#                     break
#             if 1 not in board[row_idx]:
#                 print(board)
#                 queen_p = board[row_idx-1].index(1)
#                 if queen_p + 1 < N:
#                     board[row_idx-1][queen_p], board[row_idx-1][queen_p+1] = board[row_idx-1][queen_p+1], board[row_idx-1][queen_p]
#                 else:
#                     break
#         if count_queen(board) == N:
#             count += 1
#         for row in board:
#             print(row)
#         print('--------------------')
#         board = [[0 for i in range(N)] for j in range(N)]
#
#
#     print('#{} {}'.format(test_case, count))

