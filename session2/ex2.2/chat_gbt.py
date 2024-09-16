class SchoolClass:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.average_age = 0
        self.average_height = 0
        self.average_weight = 0

    def add_student(self, age, height, weight):
        self.students.append((age, height, weight))

    def calculate_averages(self):
        if not self.students:
            return

        total_age = 0
        total_height = 0
        total_weight = 0

        for student in self.students:
            total_age += student[0]
            total_height += student[1]
            total_weight += student[2]

        self.average_age = total_age / len(self.students)
        self.average_height = total_height / len(self.students)
        self.average_weight = total_weight / len(self.students)


classA = SchoolClass("A")
classB = SchoolClass("B")

# Reading input for class A
num_students_A = int(input())
for _ in range(num_students_A):
    age, height, weight = map(float, input().split())
    classA.add_student(age, height, weight)

# Reading input for class B
num_students_B = int(input())
for _ in range(num_students_B):
    age, height, weight = map(float, input().split())
    classB.add_student(age, height, weight)

# Calculating averages for both classes
classA.calculate_averages()
classB.calculate_averages()

# Printing average values for each class
print(f"{classA.average_age:.2f} {classA.average_height:.2f} {classA.average_weight:.2f}")
print(f"{classB.average_age:.2f} {classB.average_height:.2f} {classB.average_weight:.2f}")

# Determining and printing the class with the higher average height
if classA.average_height > classB.average_height:
    print(classA.name)
elif classB.average_height > classA.average_height:
    print(classB.name)
else:
    if classA.average_weight < classB.average_weight:
        print(classA.name)
    elif classB.average_weight < classA.average_weight:
        print(classB.name)
    else:
        print("Same")
