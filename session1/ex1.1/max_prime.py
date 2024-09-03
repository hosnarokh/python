def is_prime(number):
    if number < 2:
        return False
    for i in range(1, number):
        if number % i == 0 and i != 1:
            return False
    return True


def calc_maghsoom(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0 and is_prime(i):
            count += 1
    return count


number = max_maghsom = 0
for i in range(10):
    input_num = int(input())
    value = calc_maghsoom(input_num)
    if value > max_maghsom or (value == max_maghsom and input_num > number):
        max_maghsom = value
        number = input_num
print(number, max_maghsom)
"""
chat gbt code:
import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def calc_maghsoom(number):
    count = 0
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            if i == (number // i):
                count += 1
            else:
                count += 2
    return count

inputs = [int(input()) for _ in range(10)]
max_maghsom = -1
number = -1

for input_num in inputs:
    value = calc_maghsoom(input_num)
    if value > max_maghsom or (value == max_maghsom and input_num > number):
        max_maghsom = value
        number = input_num

print(number, max_maghsom)
"""
