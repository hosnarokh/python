class SchoolClass:
    def __int__(self):
        self.students_height = []
        self.students_weight = []
        self.students_ages = []
        self.student_number = 0

    def calc_avg_ages(self):
        return sum(self.students_ages) / self.student_number

    def calc_avg_height(self):
        return sum(self.students_height) / self.student_number

    def calc_avg_wight(self):
        return sum(self.students_weight) / self.student_number

    def fill_data(self):
        self.student_number = int(input())
        self.students_ages = list(map(int, input().split()))
        self.students_height = list(map(int, input().split()))
        self.students_weight = list(map(int, input().split()))


class Analysis:
    def __init__(self, first_class: SchoolClass, second_class: SchoolClass):
        self.first_class = first_class
        self.second_class = second_class

    def compare(self):
        result = ''
        if self.first_class.calc_avg_height() > self.second_class.calc_avg_height():
            result = "A"
        elif self.first_class.calc_avg_height() == self.second_class.calc_avg_height():
            if self.first_class.calc_avg_wight() < self.second_class.calc_avg_wight():
                result = 'A'
            elif self.first_class.calc_avg_wight() == self.second_class.calc_avg_wight():
                result = 'Same'
            else:
                result = 'B'


        else:
            result = 'B'
        return result


class_a = SchoolClass()
class_a.fill_data()
class_b = SchoolClass()
class_b.fill_data()
compare_ab = Analysis(class_a, class_b)
print(class_a.calc_avg_ages())
print(class_a.calc_avg_height())
print(class_a.calc_avg_wight())
print(class_b.calc_avg_ages())
print(class_b.calc_avg_height())
print(class_b.calc_avg_wight())
print(compare_ab.compare())
