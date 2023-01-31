# Завдання 1
print(' 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності, \n'
      'закон якої задається за допомогою функції користувача. Крім цього параметром генераторної функції повинні бути \n'
      'значення першого члена прогресії та кількість членів, що видаються послідовностю. Генератор повинен зупинити \n'
      'свою роботу або по досягненню n-го члена, або при передачі команди на завершення.')
from math import cos


def generator(first_num: int, nums_len: int, func):
    for i in range(nums_len):
        yield func(first_num)
        first_num += 1
        i += 1


def cos_func(num: int):
    return cos(num)


for i in generator(1, 10, cos_func):
    print(i)

# Завдання 2
print(' 2. Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація \n'
      'https://en.wikipedia.org/wiki/Memoization. Використовуйте отриманий механізм для прискорення функції \n'
      'рекурсивного обчислення n - го члена ряду Фібоначчі. Порівняйте швидкість виконання із просто рекурсивним підходом.')


def memoization(n):
    memo = {}

    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        result = n
    else:
        result = memoization(n - 1) + memoization(n - 2)


    memo[n] = result
    return result


def recursion(n):
    if n == 0 or n == 1:
        return n
    else:
        return recursion(n - 1) + recursion(n - 2)


n = 10

import time

start = time.time()
print(recursion(n))
print('Time taken by recursion is: ', time.time() - start)


start = time.time()
print(memoization(n))
print('Time taken by memoization is: ', time.time() - start)


# Завдання 3
print(' 3. Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів \n'
      'отриманого списку.')


def some_func(change_list: list, func):
    return sum([func(i) for i in change_list])

some_list = [5, 3, 7, 3, 1, 5, 7, 3]
print(some_list)


def square(x):
    return x ** 2

print(some_func(some_list, square))




