# Рознесіть класи, які використовували під час вирішення завдання про замовлення та групу студентів по модулям.
# Переконайтеся у працездатності проєктів.
import Homework_OOP4_Module_Human
import Homework_OOP4_Module_Student
import Homework_OOP4_Module_Group

group = Homework_OOP4_Module_Group.Group('IT Gen', max_students=10)
group.add_student(Homework_OOP4_Module_Student.Student('Maksymova', 'Mariia', 'female', 26))
group.add_student(Homework_OOP4_Module_Student.Student('Ivasiv', 'Ivan', 'male', 35))
group.add_student(Homework_OOP4_Module_Student.Student('Vasiv', 'Vasyl', 'male', 22))
group.add_student(Homework_OOP4_Module_Student.Student('Oleskiv', 'Olesya', 'female', 23))
group.add_student(Homework_OOP4_Module_Student.Student('Avdiiv', 'Anna', 'female', 24))
group.add_student(Homework_OOP4_Module_Student.Student('Dmytrenko', 'Dariia', 'female', 21))
group.add_student(Homework_OOP4_Module_Student.Student('Osadchenko', 'Ostap', 'male', 27))
group.add_student(Homework_OOP4_Module_Student.Student('Markiv', 'Mark', 'male', 23))
group.add_student(Homework_OOP4_Module_Student.Student('Boykiv', 'Bogdan', 'male', 42))
group.add_student(Homework_OOP4_Module_Student.Student('Soroka', 'Serhii', 'male', 39))
group.add_student(Homework_OOP4_Module_Student.Student('Kvitka', 'Kateryna', 'female', 31))

print(group)

search = group.search_student('Soroka')
for student in search:
    print(student.surname, student.name, student.gender, student.age)



