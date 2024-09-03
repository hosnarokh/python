def movie_type():
    count_of_person = int(input())
    data = []
    result = {}
    type_of_movies = ['Horror', 'Romance', 'Comedy', 'History', 'Adventure', 'Action']
    for _ in range(count_of_person):
        data.append(input().split())
    for movie in type_of_movies:
        count_of_type = 0
        for person in data:
            count_of_type += person.count(movie)
        result[movie] = count_of_type
    sorted_data = dict(sorted(result.items(), key=lambda x: (-x[1], x[0])))
    for key, value in sorted_data.items():
        print(f'{key} : {value}')


movie_type()
