import sys
sys.stdin = open('d3_1215_input.txt', 'r')

for test_case in range(1, 11):
    word_len = int(input())
    layout = [list(input()) for j in range(8)]
    count = 0

    # 가로 palindrome 찾기
    for hor_line in layout:
        for hor_idx in range(9-word_len):
            hor_word = ''.join(hor_line[hor_idx:hor_idx+word_len])
            if hor_word == hor_word[-1::-1] and len(hor_word) == word_len:
                count += 1

    # 세로 palindrome 찾기
    for hor_idx in range(8):
        for ver_idx in range(9-word_len):
            ver_word = ''
            for space in range(ver_idx, ver_idx+word_len):
                ver_word += layout[space][hor_idx]
                if ver_word == ver_word[-1::-1] and len(ver_word) == word_len:
                    count += 1
    print('#{} {}'.format(test_case, count))