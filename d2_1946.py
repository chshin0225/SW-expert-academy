T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    letters = {}
    for i in range(N):
        letter = input().split(' ')
        letters[letter[0]] = int(letter[1])
    space = 0
    print('#{}'. format(test_case))
    for k, v in letters.items():
        for i in range(v):
            print(k, end='')
            space += 1
            if space % 10 == 0:
                print()
    print()