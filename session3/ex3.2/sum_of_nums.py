str_input = input()
count_3 = str_input.count('3')
count_2 = str_input.count('2')
count_1 = str_input.count('1')
result = ''
for i in range(count_1):
    result += '1+'

for i in range(count_2):
    result += '2+'
for i in range(count_3):
    result += '3+'
print(result[:-1])
