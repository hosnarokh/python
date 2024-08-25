from math import sqrt
count_num = int(input())
result=[]
for num in range(count_num):
    result.append(sqrt(int(input())))

for num in result:
    print(f'{num:.4f}')