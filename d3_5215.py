T = int(input())

for test_case in range(1, T+1):
    N, L = map(int, input().split())
    ingredients = [[int(i) for i in filter(None, input().split())] for _ in range(N)]

    max_score = 0
    for i in range(len(ingredients)):
        score = ingredients[i][0]
        cal = ingredients[i][1]
























    # # 부분집합 구하기
    # subsets = []
    # for i in range(1 << N):
    #     subset = []
    #     for j in range(N):
    #         if i & (1 << j):
    #             subset.append(ingredients[j])
    #     if subset:
    #         subsets.append(subset)
    #
    # max_score = 0
    # for subset_idx in range(len(subsets)):
    #     score = 0
    #     cal = 0
    #     for i in range(len(subsets[subset_idx])):
    #         score += subsets[subset_idx][i][0]
    #         cal += subsets[subset_idx][i][1]
    #     if cal > L:
    #         continue
    #     elif score > max_score:
    #         max_score = score
    # print('#{} {}'.format(test_case, max_score))
