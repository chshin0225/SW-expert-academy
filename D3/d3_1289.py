import sys
sys.stdin = open('d3_1289_input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    original_memory = [int(i) for i in input()]
    print(original_memory)
    memory = [0] * len(original_memory)
    times = 1
    num_change = 0
    while True:
        try:
            if times % 2:
                new_num = 1
            else:
                new_num = 0
            num_change += original_memory.index(new_num)
            print('num change', num_change)
            memory = memory[:num_change] + [new_num] * (len(memory)-num_change)
            print('memory', memory)
            times += 1
            original_memory = original_memory[num_change:]
            print('original_memory', original_memory)
            print('-------------------------------')
        except:
            break
    print(memory)
    print(times)
            
