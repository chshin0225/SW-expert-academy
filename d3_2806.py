import sys
sys.stdin = open('d3_2806_input.txt', 'r')

# 퀸을 하나 놓을 때, 이 위치에 놓으면 다른 퀸들을 죽이는지 알려주는 함수 정의
def queen(row):
    global cols
    global cnt

    def possible(row):
        for i in range(1, row):
            if cols[i] == cols[row]:
                return False
            if abs(i - row) == abs(cols[i] - cols[row]):
                return False
        return True

    if row == N+1:
        cnt += 1
        return
    for j in range(1, N+1):
        cols[row] = j
        if not possible(row):
            continue
        queen(row+1)


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cols = [0] * (N+1)    # 1~N행: 몇번째 열에 체스가 놓여있는지 보여줌
    cnt = 0
    queen(1)
    print('#{} {}'.format(test_case, cnt))































# # 퀸을 하나 놓을 때, 이 위치에 놓으면 다른 퀸들을 죽이는지 알려주는 함수 정의
# def queen(row, N):
#     global cols
#     global cnt
#
#     def possible(cols, row, col):
#         # 대각선 탐색
#         if col not in cols:
#             for r in range(1, row):
#                 if abs(r - row) == abs(cols[r] - col):
#                     return False
#         # 세로 탐색
#         elif col in cols:
#             return False
#         return True
#
#     if row == N+1:
#         print('answer', cols)
#         cnt += 1
#         return
#     for c in range(1, N+1):
#         cols[row] = c
#         if not possible(cols, row, c):
#             continue
#         queen(row+1, N)
#
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     N = int(input())
#     cols = [0] * (N+1)    # 1~N행: 몇번째 열에 체스가 놓여있는지 보여줌
#     cnt = 0
#     queen(1, N)
#     print('#{} {}'.format(test_case, cnt))



