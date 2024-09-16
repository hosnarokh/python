def movie_type():
    count_of_person = int(input())
    data = []
    for _ in range(count_of_person):
        data.append([var for var in input().split('.')])

    sorted_data = sorted(data, key=lambda x: (x[0].lower(), x[1].lower()))

    for person in sorted_data:
        print(f'{person[0]} {person[1].capitalize()} {person[2]}')


movie_type()



"""
def standardize_name(name):
    parts = name.split('.')
    gender = parts[0]
    name_parts = parts[1].split()
    first_name = name_parts[0].capitalize()
    last_name = ' '.join([part.capitalize() for part in name_parts[1:]])
    language = parts[-1]
    
    return f"{gender} {first_name} {last_name} {language}"

# Reading the number of participants
n = int(input())

# Reading and processing participant names
participants = [input() for _ in range(n)]

# Separating names based on gender
male_participants = [name for name in participants if name.startswith('m')]
female_participants = [name for name in participants if name.startswith('f')]

# Sorting names alphabetically
male_participants.sort(key=lambda x: x.split('.')[1].split()[0])
female_participants.sort(key=lambda x: x.split('.')[1].split()[0])

# Standardizing and printing names
for female_name in female_participants:
    print(standardize_name(female_name))

for male_name in male_participants:
    print(standardize_name(male_name))
"""
