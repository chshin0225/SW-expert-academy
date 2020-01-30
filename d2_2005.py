# T = int(input())
T = 1

for test_case in range(1, T+1):
    # N = int(input())
    N = 4
    layout = [[0 if (j != 0 and j != j-1) else 1 for j in range(j)] for j in range(1, N+1)]
    # for line in layout:
    #     for space in line:
    #         if space == line[0]:
    #             line[space] = 1
    #         if space == line[-1]:
    #             line[space] = 1
    print(test_case)
    print(layout)