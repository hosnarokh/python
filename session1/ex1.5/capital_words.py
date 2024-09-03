def find_capital_words():
    text = input().split('.')
    has_capital = False
    words = [sentence.split() for sentence in text]
    capital_words = {}
    word_count = 0
    for sentence in words:
        word_count += 1
        for i in range(1, len(sentence)):
            word_count += 1
            if sentence[i].replace('.', "").replace(";", '') == sentence[i].capitalize():
                capital_words[word_count] = sentence[i]
    for key, value in capital_words.items():
        print(f'{key}:{value}')
        has_capital = True
    if not has_capital:
        print(None)


find_capital_words()
