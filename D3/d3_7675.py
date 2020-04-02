import sys
sys.stdin = open('d3_7675_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    counts = [0 for _ in range(N)]
    string = input()
    punctuations = [letter for letter in string if letter in ['!', '?', '.']]
    sentences = []
    for punctuation in punctuations:

    print(sentences)