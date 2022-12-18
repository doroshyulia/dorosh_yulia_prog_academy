# 2. Модифікуйте Друге домашнє завдання так, щоб при спробі додавання до групи більше 10-ти студентів, викликалася
# виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати). Подію додавання нового студента до групи
# необхідно фіксувати у лог-файлі.
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)


class MyError(Exception):
    def __init__(self, max_limit):
        self.max_limit = max_limit

    def __str__(self):
        return f'Sorry, we already have {self.max_limit} students in this group.'
	
	
class DublicateError(Exception):
	def __init__(self, student, group):
        self.student = student
	self.group_name = group

    def __str__(self):
        return f'Sorry, but {self.student} has already enrolled in this group.'


class Human:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    def __str__(self):
        return f'{self.surname} {self.name}'


class Student(Human):
    def __init__(self, surname, name, gender, age):
        super().__init__(surname, name)
        self.gender = gender
        self.age = age

    def __str__(self):
        return f'{super().__str__()}, {self.gender}, {self.age}'


class Group:
    def __init__(self, group_name, max_students=10):
        if max_students <= 0:
            raise ValueError()
        self.group_name = group_name
        self.students = []
        self.max_students = max_students

    def add_student(self, student):
        if student in self.students:
		raise DublicateError(student, self.group_name)
	if len(self.students) >= self.max_students:
		raise MyError(self.max_students)
                
        self.students.append(student)             

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def search_student(self, surname):
        result = []
        for student in  self.students:
            if student.surname == surname:
                result.append(student)
                return result

    def __str__(self):
        return f'{self.group_name}\n' + '\n'.join(map(str, self.students))


try:
    group = Group('IT Gen', max_students=10)
    group.add_student(Student('Maksymova', 'Mariia', 'female', 26))
    group.add_student(Student('Ivasiv', 'Ivan', 'male', 35))
    group.add_student(Student('Vasiv', 'Vasyl', 'male', 22))
    group.add_student(Student('Oleskiv', 'Olesya', 'female', 23))
    group.add_student(Student('Avdiiv', 'Anna', 'female', 24))
    group.add_student(Student('Dmytrenko', 'Dariia', 'female', 21))
    group.add_student(Student('Osadchenko', 'Ostap', 'male', 27))
    group.add_student(Student('Markiv', 'Mark', 'male', 23))
    group.add_student(Student('Boykiv', 'Bogdan', 'male', 42))
    group.add_student(Student('Soroka', 'Serhii', 'male', 39))
    group.add_student(Student('Kvitka', 'Kateryna', 'female', 31))

    logging.debug(group)

except Exception as error:
    print(error)
