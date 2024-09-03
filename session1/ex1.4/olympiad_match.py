def movie_type():
    count_of_person = int(input())
    data = []
    for _ in range(count_of_person):
        data.append([var for var in input().split('.')])

    sorted_data = sorted(data, key=lambda x: (x[0].lower(), x[1].lower()))

    for person in sorted_data:
        print(f'{person[0]} {person[1].capitalize()} {person[2]}')


movie_type()
