input_str = input()
i = 0
sub = 'hello'
new_string = ''
j = 0
for new_char in sub[j:]:
    for char in input_str[i:]:
        i += 1
        if new_char == char:
            j += 1
            new_string += new_char
            break

if new_string == sub:
    print('YES')
else:
    print('NO')
