city_count = int(input())
data = {}
sentences = ''
for i in range(0, city_count + 1):
    if i == city_count:
        sentences = input().split()
        break
    new_word = input().split()
    data[new_word[0]] = new_word[1]

result = ''
for word in sentences:
    result += f'{data.get(word, word)} '
print(result)
