# Завдання №1
print('Реализуйте метакласс, который обладает следующим функционалом: при его использовании в файл с заранее\n'
      'определенным названием нужно сохранить имя класса и список его полей.')

class MetaClass(type):
    def __init__(cls, name, bases, dct):
        super(MetaClass, cls).__init__(name, bases, dct)
        with open('class_info.txt', 'a') as f:
            f.write(f'Class name: {name}\n')
            f.write(f'Fields: {list(dct.keys())}\n')

class MyClass(metaclass=MetaClass):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

my_class = MyClass('Ivan', 'Soroka')