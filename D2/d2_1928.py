import base64

num_of_test_cases = int(input('number of test case?'))

for i in range(1, num_of_test_cases+1):
    string = input('message?')
    string_byte = string.encode('ASCII')
    decoded_string = base64.b64decode(string_byte)
    message = decoded_string.decode('ASCII')
    result = '#{} {}'.format(i, message)
    print(result)