import random

result_compar = ''
start = 1
end = 100
while result_compar != 'd':
    hads = random.randint(start, end)
    print(hads)
    result_compar = input()
    if result_compar == 'k':
        end = hads
    elif result_compar == 'b':
        start = hads
