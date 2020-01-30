T = int(input())

for test_case in range(T):
    test_case_no = int(input())
    scores = [int(i) for i in filter(None, input().split(' '))]
print(scores)