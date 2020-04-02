import sys
sys.stdin = open('d3_4615_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0 for i in range(N)] for j in range(N)]

    # 초기 설정
    board[N//2-1][N//2-1] = board[N//2][N//2] = 2
    board[N//2-1][N//2] = board[N//2][N//2-1] = 1

    # 순차적으로 돌을 놓기
    for turn in range(M):
        x, y, c = [int(i) for i in input().split()]
        # 인덱스랑 맞추기 위해 1씩 빼기
        x -= 1
        y -= 1
        # 돌을 위치에 놓기
        board[x][y] = c
        # 내가 누구냐에 따라 상대방 지정
        opponent = 2 if c == 1 else 1

        for find_x in range(x - 1, x + 2):
            for find_y in range(y - 1, y + 2):
                # 존재하지 않는 좌표이거나 자기 자신일 경우 배제
                if find_x < 0 or find_y < 0 or find_y >= N or find_x >= N or (find_x == x and find_y == y):
                    continue
                # 주변에 상대편 돌을 찾기
                if board[find_x][find_y] == opponent:
                    # 내가 놓은 돌과 상대의 돌의 차이 구하기
                    diff_x = find_x - x
                    diff_y = find_y - y

                    new_x, new_y = find_x, find_y
                    # 이제 점점 직선 방향으로 움직이면서 어디까지 상대방 돌이 있는지, 상대방 돌들을 뒤집을 수 있기 위한 나의 돌이 있는지
                    while 0 <= new_x < N and 0 <= new_y < N:
                        if board[new_x][new_y] == 0:
                            result = False
                            break
                        if board[new_x][new_y] == c:
                            result = True
                            break
                        new_x += diff_x
                        new_y += diff_y
                        result = False

                    if result == True:
                        cx, cy = x, y
                        while [cx, cy] != [new_x, new_y]:
                            board[cx][cy] = c
                            cx += diff_x
                            cy += diff_y

        b_count = 0
        w_count = 0
        for row in board:
            for space in row:
                if space == 1:
                    b_count += 1
                elif space == 2:
                    w_count += 1

    print('#{} {} {}'.format(test_case, b_count, w_count))