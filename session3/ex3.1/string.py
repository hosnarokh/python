str_input = input()
vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
out_put = str_input
for char in set(str_input):
    if char in vowels:
        out_put = out_put.replace(char, "")
    else:
        out_put = out_put.replace(char, f".{char}")

print(out_put.lower())