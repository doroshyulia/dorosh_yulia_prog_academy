# Завдання №1
print(' 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії із зазначеним \n'
      'множником.Генератор повинен зупинити свою роботу або після досягнення зазначеного елементу, або при передачі\n'
      'команди на завершення.')


def geom_prog(multipler, stop_element):
    element = 1
    while element <= stop_element:
        yield element
        element *= multipler
        if element > stop_element:
            return


for n in geom_prog(2, 20):
    print(n)

# Завдання №2
print(' 2. Реалізуйте свій аналог генераторної функції range().')


def my_copy_range(start, end, step=1):
    numbers = []
    for i in range(start, end, step):
        numbers.append(i)
    return numbers


print(my_copy_range(0, 10))

# Завдання №3
print(' 3. Напишіть функцію-генератор, яка повертатиме прості числа. Верхня межа діапазону повинна бути задана \n'
      'параметром цієї функції')


def prime_num(limit):
    for num in range(2, limit + 1):
        divider = 2
        while divider < num:
            if not num % divider:
                break
            divider += 1
        else:
            yield num
    return


g = prime_num(5)
print(next(g))
print(next(g))
print(next(g))


# Завдання №4
print(' 4. Напишіть генераторний вираз для заповнення списку. Список повинен бути заповнений кубами чисел від 2 до \n'
      'вказаної вами величини.')


def my_func(finish):
    cubes = []
    for start in range(2, finish + 1):
        yield start ** 3
        cubes.append(start ** 3)
    return cubes


for i in my_func(6):
    print(i)

