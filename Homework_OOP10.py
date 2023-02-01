# Завдання №1
print('1) Создайте декоратор, который зарегистрирует декорируемый класс в списке классов.')


def register_class(cls):
    classes = []
    classes.append(cls)
    def decorator(cls):
        return cls
    return decorator

@register_class
class MyClass:
    pass


print(MyClass)


# Завдання №2
print('Создайте декоратор класса с параметром. Параметром должна быть строка, которая должна дописываться (слева) к \n'
      'результату работы метода str.')


def my_decorator(str):
    def decorator(cls):
        class Wrapper(cls):
            def __str__(self):
                return str + super().__str__()
        return Wrapper
    return decorator


@my_decorator('Hi, ')
class MyClass:
    def __str__(self):
        return 'stranger!'

print(MyClass())


# Завдання №3
print('Для класса Box напишите статический метод, который будет подсчитывать суммарный объем двух ящиков, которые\n'
      ' будут его параметрами.')


class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    @staticmethod
    def total_volume(box_1, box_2):
        return box_1.length * box_1.width * box_1.height + box_2.length * box_2.width * box_2.height


first_box = Box(2, 3, 4)
second_box = Box(5, 6, 7)

print(Box.total_volume(first_box,second_box))
