def is_number(x):
    if x.isdigit():
        return True
    return False

# in-stack priority
def isp(token):
    if token == '*':
        return 2
    elif token == '+':
        return 1
    elif token == '(':
        return 0

# in-coming priority
def icp(token):
    if token == '*':
        return 2
    elif token == '+':
        return 1
    elif token == '(':
        return 3

def calculate(x, n1, n2):
    if x == '+':
        return n2 + n1
    elif x == '*':
        return n2 * n1


for test_case in range(1, 11):
    N = int(input())
    cal = input()
    li = ['+', '*']
    # 중위에서 후위 변환
    postfix = []
    stack = []
    for i in cal:
        if is_number(i):
            postfix.append(i)
        elif not stack:
            stack.append(i)
        elif i == ')':
            while stack:
                p = stack.pop()
                if p == '(':
                    break
                postfix.append(p)
        elif icp(i) > isp(stack[len(stack) - 1]):
            stack.append(i)
        else:
            while True:
                s = stack.pop()
                if icp(i) > isp(s):
                    stack.append(s)
                    stack.append(i)
                    break
                postfix.append(s)

    # 계산하기
    li2 = ['*', '+']
    stack = []
    for p in postfix:
        if is_number(p):
            stack.append(int(p))
        elif p in li2:
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(calculate(p, n1, n2))
    result = stack.pop()

    print('#{} {}'.format(test_case, result))