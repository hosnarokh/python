city_count = int(input())
data = {}
for i in range(city_count):
    new_city = input()
    data[new_city] = data.get(new_city, 0) + 1

for key, value in dict(sorted(data.items(), key=lambda x: x[0])).items():
    print(key, value)
