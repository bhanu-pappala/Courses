def str_to_int(input_str):
    if input_str[0] == '-':
        is_negative = True
        start_ind = 1
    else:
        is_negative = False
        start_ind = 0

    output_int = 0
    
    for i in range(start_ind, len(input_str)):
        place = 10 ** (len(input_str) - (i + 1))
        digit = ord(input_str[i]) - ord('0')
        output_int += place * digit

    if is_negative:
        return -1 * output_int
    else:
        return output_int

s = "554"
x = str_to_int(s)
print(type(x))

s = "123"
print(str_to_int(s))

s = "-123"
print(str_to_int(s))
