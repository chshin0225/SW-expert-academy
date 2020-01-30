import sys
# 표준 입력을 바꾸기(standard in)
sys.stdin = open('d2_1206_input.txt', 'r')

T = 10
for tc in range(1, 1+T):
    N = int(input()) # 빌딩수
    h = list(map(int, input().split())) # 높이배열
    view = 0 # 조망권 수
    for i in range(2, N-2):    # 앞뒤로 2칸은 빌딩이 없으므로 제외
        left = h[i-2] if (h[i-2] > h[i-1]) else h[i-1] # 왼쪽 2개 빌딩 중 최고층 빌딩
        right = h[i+1] if (h[i+1] > h[i+2]) else h[i+2] # 오른쪽 2개 빌딩 중 최고층 빌딩
        t = left if (left > right) else right    # 가독성을 위해 조건을 괄호에 넣는 것
        # 위에 세 줄을 파이썬 함수 이용하여 풀기
        # t = max(h[i-2], h[i-1], h[i+1], h[i+2])
        if (h[i] > t):
            view = view + h[i] - t    # 조망권 세대수 누적합
    print('#{} {}'.format(tc, view))