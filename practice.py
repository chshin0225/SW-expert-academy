# 재귀로 부분집합 만들기

def f(n, k):
    if n == k:
        for i in range(k):
            if b[i] == 1:
                print(b[i], end=' ')
        print()
    else:
        b[n] = 1
        f(n+1, k)
        b[n] = 0
        f(n+1, k)
arr = [1, 2, 3]
b = [0] * len(arr)
f(0, len(arr))


