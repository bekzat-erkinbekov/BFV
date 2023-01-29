class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.married = is_married

    def introduce_myself(self):
        print(f'Fullname: {self.fullname}\n'
              f'Age: {self.age}\n'
              f'is married?: {self.married}')

class Student(Person):
    def __init__(self, fullname, age, is_married, marks:dict):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average(self):
        return sum(self.marks.values()) / len(self.marks.values())

class Teacher(Person):
    salary = 15000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def zarplata(self):
        return self.salary + ((self.salary / 100 * 5) * (self.experience - 3)) if self.experience > 3 else self.salary

uchitel = Teacher('Bekzat', 20, False, 3)

print(f'fullname: {uchitel.fullname}\n'
      f'age: {uchitel.age}\n'
      f'married: {uchitel.married}\n'
      f'experience: {uchitel.experience}\n'
      f'salary: {uchitel.zarplata()}\n')

def create_student():
    student1 = Student('Max1', 13, False, marks={
        'bio': 3,
        'math': 5,
        'geom': 4
    })

    student2 = Student('Max2', 15, False, marks={
        'bio': 3,
        'math': 5,
        'geom': 2
    })

    student3 = Student('Max3', 32, True, marks={
        'bio': 5,
        'math': 5,
        'geom': 5,
        'chemistry': 3
    })

    lst = [student1, student2, student3]
    return lst

spisok = create_student()

for i in spisok:
    print(f'fullname: {i.fullname}\n'
          f'age: {i.age}\n'
          f'married: {i.married}\n'
          f'average_marks: {i.average()}\n')

