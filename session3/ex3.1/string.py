str_input = input()
vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')

for char in str_input:
    if char in vowels:
        str_input = str_input.replace(char, "")
    else:
        str_input = str_input.replace(char, f".{char}")

print(str_input.lower())


