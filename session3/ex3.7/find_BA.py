input_str = input()
index_ab = input_str.upper().find('AB')
if index_ab > -1 and (input_str.upper()[:index_ab].find('BA') > -1 or input_str.upper()[index_ab + 2:].find('BA') > -1):
    print('YES')
else:
    print('NO')
