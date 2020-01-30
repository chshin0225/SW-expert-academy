# num_of_test_case = int(input('number of test case?'))
num_of_test_case = 1

for i in range(1, num_of_test_case+1):
    case = [list(map(lambda x: int(x), input('case?').split(' '))) for j in range(9)]
    for line in case:
        if len(set(line)) != 9:
            print('#{} 0'.format(i))
            break
    else:
        ver_lines = {}
        for ver_line in range(9):
            ver_lines[ver_line] = []
            for line in case:
                ver_lines[ver_line].append(line[ver_line])
        for k, v in ver_lines.items():
            if len(set(v)) != 9:
                print('#{} 0'.format(i))
                break
        else:
            print('#{} 1'.format(i))
