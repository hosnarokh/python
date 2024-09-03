# For the average
import csv
from statistics import mean


def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        data = {}
        for row in reader:
            name = row[0]
            grades = []
            for grade in row[1:]:
                grades.append(float(grade))
            data[name] = mean(grades)
    with open(output_file_name, mode='w') as f:
        for name, avg in data.items():
            f.write(f'{name},{avg}\n')


def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        data = {}
        for row in reader:
            grades = []
            name = row[0]
            for grade in row[1:]:
                grades.append(float(grade))
            data[name] = mean(grades)

    sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))
    with open(output_file_name, mode='w') as f:
        for name, avg in sorted_data.items():
            f.write(f'{name},{avg}\n')


def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        data = {}
        for row in reader:
            grades = []
            name = row[0]
            for grade in row[1:]:
                grades.append(float(grade))
            data[name] = mean(grades)

    sorted_data = dict(sorted(data.items(), key=lambda x: x[1])[-3:])
    with open(output_file_name, mode='w') as f:
        for name, avg in sorted_data.items():
            f.write(f'{name},{avg}\n')


def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        data = {}
        for row in reader:
            grades = []
            name = row[0]
            for grade in row[1:]:
                grades.append(float(grade))
            data[name] = mean(grades)

    sorted_data = dict(sorted(data.items(), key=lambda x: x[1])[:3])
    with open(output_file_name, mode='w') as f:
        for name, avg in sorted_data.items():
            f.write(f'{avg}\n')


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        data = {}
        for row in reader:
            grades = []
            name = row[0]
            for grade in row[1:]:
                grades.append(float(grade))
            data[name] = mean(grades)

    avg = mean(data.values())
    with open(output_file_name, mode='w') as f:
        f.write(f'{avg}\n')


calculate_averages('data.csv','avg.csv')
calculate_sorted_averages('data.csv','sorted_avg.csv')
calculate_three_best('data.csv','best_three.csv')
calculate_three_worst('data.csv','three_worst.csv')
calculate_average_of_averages('data.csv','avg_avg.csv')