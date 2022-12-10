# 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# 2. На його основі створіть клас Студент (перевизначте метод виведення інформації).
# 3. Створіть клас Група, який містить масив із 10 об'єктів класу Студент. Реалізуйте методи додавання, видалення
# студента та метод пошуку студента за прізвищем. Визначте для Групи метод str() для повернення списку студентів у
# вигляді рядка.


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
        self.group_name = group_name
        self.students = []
        self.max_students = max_students

    def add_student(self, student):
        if student not in self.students and len(self.students) < self.max_students:
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

print(group)

search = group.search_student('Soroka')
for student in search:
    print(student.surname, student.name, student.gender, student.age)


