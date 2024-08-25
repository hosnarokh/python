import csv
import hashlib


def hash_password_hack(input_file_name, output_file_name):
    hash_dict = {}
    for i in range(1000, 10000):
        hash_dict[hashlib.sha256(str(i).encode('utf-8')).hexdigest()] = i

    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            password = hash_dict.get(row[1])
            print(f'{name},{password}')
