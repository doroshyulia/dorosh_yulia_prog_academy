# Завдання №1
print(' 1. Создайте декоратор, который будет подсчитывать, сколько раз была вызвана декорируемая функция.')


def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@count_calls
def somefunc(n):
    return n * 5


@count_calls
def otherfunc(n):
    return n * 10


print(somefunc(4))
print(otherfunc(2))
print(otherfunc(3))
print(otherfunc.calls)


# Завдання №2
print(' 2. Создайте декоратор, который зарегистрирует декорируемую функцию в списке функций, для обработки \n'
      'последовательности.')

registered_funcs = []
def register_func(func):
    registered_funcs.append(func)
    return func


@register_func
def userfunc1(f):
    return f*10

@register_func
def userfunc2(f):
    return f*20

print(userfunc1(3))
print(userfunc2(5))
print(registered_funcs)


# Завдання №3
print(' 3. Предположим, в классе определен метод __str__, который возвращает строку на основании класса. \n'
      'Создайте такой декоратор для этого метода, чтобы полученная строка сохранялась в текстовый файл, имя которого \n'
      'совпадает с именем класса, метод которого вы декорировали.')


def save_to_file(func):
    def wrapper(*args, **kwargs):
        file_name = f"{func.__qualname__.split('.')[0]}.txt"
        result = func(*args, **kwargs)
        with open(file_name, 'a') as f:
            f.write(f'{result}\n')
        return result
    return wrapper


class Str:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @save_to_file
    def __str__(self):
        return f'{self.x * self.y}'


x = Str(2, 5)
print(x)
y = Str(3, 7)
print(y)


# Завдання №4
print('4. Создайте декоратор с параметрами для проведения хронометража работы той или иной функции. Параметрами должны\n'
      ' выступать то, сколько раз нужно запустить декорируемую функцию и в какой файл сохранить результаты хронометража\n'
      ' Цель - провести хронометраж декорируемой функции.')

import time


def chronometer(func, file_name: str = "chronometer.txt", counter: int = 15):
    def wrapper(*args, **kwargs):
        total_time = 0
        for _ in range(counter):
            start_time = time.perf_counter()
            x = func(*args, **kwargs)
            stop_time = time.perf_counter()
            total_time += (stop_time - start_time)
        with open(file_name, 'w') as f:
            f.write(f'{total_time/counter:.15f}')
            return x
    return wrapper


@chronometer
def mul(x, y):
    return x * y
print(mul(2, 5))

