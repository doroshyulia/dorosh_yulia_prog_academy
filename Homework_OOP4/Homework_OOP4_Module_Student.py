import Homework_OOP4_Module_Human


class Student(Homework_OOP4_Module_Human.Human):
    def __init__(self, surname, name, gender, age):
        super().__init__(surname, name)
        self.gender = gender
        self.age = age

    def __str__(self):
        return f'{super().__str__()}, {self.gender}, {self.age}'