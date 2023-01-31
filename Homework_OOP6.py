# Завдання №1
print('# 1. Доповніть клас Група (завдання Лекції 2) можливістю підтримки ітераційного протоколу.')


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

    def __iter__(self):
        for item in self.students:
            yield item

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


# Завдання №2
print('# 2. Модифікуєте клас Замовлення (завдання Лекції 1), додавши реалізацію протоколу послідовностей та \n'
      'ітераційного протоколу.')


class Product:

    def __init__(self, product, description, dimensions, price):
        self.product = product
        self.description = description
        self.dimensions = dimensions
        self.price = price

    def __str__(self):
        return f'{self.product} {self.description},{self.dimensions}: {self.price}'


class Customer:

    def __init__(self, surname, name, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f'{self.surname} {self.name}; {self.phone_number}'


class Cart:

    def __init__(self, customer: Customer):
        self.customer = customer
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: float = 1):
        if product in self.products:
            index = self.products.index(product)
            self.quantities[index] += quantity
        else:
            self.products.append(product)
            self.quantities.append(quantity)

    def total(self):
        return sum(item.price * self.quantities[index] for index, item in enumerate(self.products))

    def __str__(self):
        res = '\n'.join(map(
            lambda item: f'{item[0]} x {item[1]} = {item[0].price * item[1]} $',
            zip(self.products, self.quantities))
        )

        return f'{customer}\n{res}\nTotal: {self.total()} $'

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index == len(self.products):
            raise StopIteration
        else:
            current_product = self.products[self.current_index]
            current_quantity = self.quantities[self.current_index]
            self.current_index += 1
            return current_product, current_quantity


lemon = Product('Lemon', 'yellow', 'on sale', 4.00)
pineapple = Product('Pineapple', 'yellow', 'first class', 7.69)
apple = Product('Apple', 'red', 'extra fresh', 2.50)

customer = Customer('Petrov', 'Petro', '+380686868686')

order = Cart(customer)
order.add_product(apple, 3)
order.add_product(pineapple)
order.add_product(lemon, 0.5)

print(order)
