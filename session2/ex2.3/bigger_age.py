final_age = 0
age = 0
while age != -1:
    age = int(input())
    if final_age < age:
        final_age = age

print(final_age)