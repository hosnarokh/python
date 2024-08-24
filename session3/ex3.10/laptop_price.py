pc_count = int(input())
pc_data = []
result = 'poor irsa'
for i in range(pc_count):
    pc_data.append(list(map(int, input().split())))
for i in range(pc_count):
    for j in range(1, pc_count):
        if pc_data[i][0] < pc_data[j][0] and pc_data[i][1] > pc_data[j][1]:
            result = 'happy irsa'
print(result)
