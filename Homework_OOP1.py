# Домашнє завдання:
# 1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару, опису
# товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
# 2. Створіть клас "Покупець". У якості атрибутів можна використовувати прізвище, ім'я, по батькові, мобільний телефон
# тощо.
# 3. Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості. Замовлення має містити дані
# про користувача, який його здійснив. Реалізуйте метод обчислення сумарної вартості замовлення. Визначте метод str()
# для коректного виведення інформації про це замовлення.


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


lemon = Product('Lemon', 'yellow', 'on sale', 4.00)
pineapple = Product('Pineapple', 'yellow', 'first class', 7.69)
apple = Product('Apple', 'red', 'extra fresh', 2.50)

customer = Customer('Petrov', 'Petro', '+380686868686')

order = Cart(customer)
order.add_product(apple, 3)
order.add_product(pineapple)
order.add_product(lemon, 0.5)

print(order)
