T = int(input())

for test_case in range(1, T + 1):
    N, K = [int(i) for i in input().split(' ')]
    scores = [[int(j) for j in input().split(' ')] for _ in range(N)]
    grade_quota = int(N / 10)
    total_scores = []
    for score in scores:
        total_score = score[0] * 35 / 100 + score[1] * 45 / 100 + score[2] * 20 / 100
        total_scores.append(total_score)
    K_score = total_scores[K - 1]
    total_scores.sort(reverse=True)
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    total_scores = [[total_scores[i] for i in range(j, j + grade_quota)] for j in range(0, N, grade_quota)]
    grades_ranked = dict(zip(grades, total_scores))
    for k, v in grades_ranked.items():
        if K_score in v:
            K_grade = k
            break
    print('#{} {}'.format(test_case, K_grade))