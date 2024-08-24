message = input()
capital = sum(1 for c in message if c.isupper())
lower_c = sum(1 for c in message if c.islower())
print(message.upper() if capital > lower_c else message.lower())
