def translate():
    words_count = int(input())
    custom_dict = {}
    for _ in range(words_count):
        words = input().split()
        for i in range(1, len(words)):
            custom_dict[words[i]] = words[0]
    # print(custom_dict)
    sentence = input().split()
    result = ''
    for word in sentence:
        translated_word = custom_dict.get(word, word)
        result += f'{translated_word} '
    print(result.strip())


translate()
