pc_count = int(input())
pc_data = []

for i in range(pc_count):
    pc_data.append(list(map(int, input().split())))
pc_data_price = sorted(pc_data, key=lambda x: x[0])
pc_data_good = sorted(pc_data, key=lambda x: x[1], reverse=True)
if pc_data_price[0][1] == pc_data_good[0][1]:
    print('happy irsa')
else:
    print('poor irsa')
