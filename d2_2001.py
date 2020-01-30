import sys
sys.stdin = open('d2_2001_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, M = [int(i) for i in input().split(' ')]
    layout = [[int(j) for j in input().split(' ')] for _ in range(N)]
    possibilities = []
    for line in range(N-M+1):
        for space in range(N-M+1):
            killed_flies = 0
            for hor_range in range(line, line+M):
                for ver_range in range(space, space+M):
                    killed_flies += layout[hor_range][ver_range]
                    possibilities.append(killed_flies)
    print(max(killed_flies))
