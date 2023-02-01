# Завдання №1
print('1. Создайте дескриптор, который будет делать поля класса управляемые им доступными только для чтения.')


class ReadOnlyDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        raise AttributeError("Can't set attribute")

class X:
    attr = ReadOnlyDescriptor(10)

#obj = X()
#obj.attr = 20


# Завдання №2
print('2.Реализуйте функционал, который будет запрещать установку полей класса любыми значениями, кроме целых чисел.\n'
      ' Т.е., если тому или иному полю попытаться присвоить, например, строку, то должно быть возбужденно исключение.')


class MyClass:
    def __init__(self):
        self.__field = None

    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, value):
        if not isinstance(value, int):
            raise ValueError('Field value must be an integer')
        self.__field = value


obj = MyClass()
#obj.field = 20
#obj.field = 'blablabla'


# Завдання №3
print('Реализуйте свойство класса, которое обладает следующим функционалом: при установки значения этого свойства в\n'
      ' файл с заранее определенным названием должно сохранятся время (когда устанавливали значение свойства) и\n'
      ' установленное значение.')


class MyClass:
    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value
        with open('my_file.txt', 'w') as f:
            f.write(f'{value} {time.time()}')
        print(f'Value {value} was set at {time.time()}')


