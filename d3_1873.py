import sys
sys.stdin = open('d3_1873_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    H, W = map(int, input().split())
    layout = [[i for i in input()] for _ in range(H)]
    N = int(input())
    commands = [j for j in input()]
    possible_positions = ['<', '>', '^', 'v']

    # 현재 전차 위치 찾기
    for x in range(len(layout)):
        for y in range(len(layout[x])):
            if layout[x][y] in possible_positions:
                current_x, current_y, current_position = [x, y, layout[x][y]]

    for command in commands:
        # 포탄 쏠 때
        if command == 'S':
            # 전차가 위를 보고 있을 때
            if current_position == '^':
                for line_idx in range(current_x, -1, -1):
                    if layout[line_idx][current_y] == '#':
                        break
                    if layout[line_idx][current_y] == '*':
                        layout[line_idx][current_y] = '.'
                        break
            # 전차가 오른쪽을 보고 있을 때
            if current_position == '>':
                for space_idx in range(current_y + 1, W):
                    if layout[current_x][space_idx] == '#':
                        break
                    if layout[current_x][space_idx] == '*':
                        layout[current_x][space_idx] = '.'
                        break
            # 전차가 아래를 보고 있을 때
            if current_position == 'v':
                for line in layout[current_x:]:
                    if line[current_y] == '#':
                        break
                    if line[current_y] == '*':
                        line[current_y] = '.'
                        break
            # 전차가 왼쪽을 보고 있을 때
            if current_position == '<':
                for space_idx in range(current_y - 1, -1, -1):
                    if layout[current_x][space_idx] == '#':
                        break
                    if layout[current_x][space_idx] == '*':
                        layout[current_x][space_idx] = '.'
                        break

        # 아래로 내려가는 명령
        elif command == 'D':
            # 못 움직일 때
            if current_x == H - 1 or layout[current_x+1][current_y] != '.':
                layout[current_x][current_y] = 'v'
            # 움직일 수 있을 때
            else:
                layout[current_x][current_y] = '.'
                layout[current_x+1][current_y] = 'v'
                current_x += 1
            current_position = 'v'

        # 오른쪽으로 가는 명령
        elif command == 'R':
            # 못 움직일 때
            if current_y == W - 1 or layout[current_x][current_y + 1] != '.':
                layout[current_x][current_y] = '>'
            else:
                layout[current_x][current_y] = '.'
                layout[current_x][current_y + 1] = '>'
                current_y += 1
            current_position = '>'

        # 위로 올라가는 명령
        elif command == 'U':
            # 못 움직일 때
            if current_x == 0 or layout[current_x - 1][current_y] != '.':
                layout[current_x][current_y] = '^'
            else:
                layout[current_x][current_y] = '.'
                layout[current_x - 1][current_y] = '^'
                current_x -= 1
            current_position = '^'

        # 왼쪽으로 가는 명령
        else:
            # 못 움직일 때
            if current_y == 0 or layout[current_x][current_y - 1] != '.':
                layout[current_x][current_y] = '<'
            else:
                layout[current_x][current_y] = '.'
                layout[current_x][current_y - 1] = '<'
                current_y -= 1
            current_position = '<'

    result = [''.join(line) for line in layout]
    print('#{}'.format(test_case), end=' ')
    for r in result:
        print(r)



