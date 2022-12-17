# Рознесіть класи, які використовували під час вирішення завдання про замовлення та групу студентів по модулям.
# Переконайтеся у працездатності проєктів.

import Homework_OOP4_Module_Product
import Homework_OOP4_Module_Customer
import Homework_OOP4_Module_Cart

lemon = Homework_OOP4_Module_Product.Product('Lemon', 'yellow', 'on sale', 4.00)
pineapple = Homework_OOP4_Module_Product.Product('Pineapple', 'yellow', 'first class', 7.69)
apple = Homework_OOP4_Module_Product.Product('Apple', 'red', 'extra fresh', 2.50)

customer = Homework_OOP4_Module_Customer.Customer('Petrov', 'Petro', '+380686868686')

order = Homework_OOP4_Module_Cart.Cart(customer)
order.add_product(apple, 3)
order.add_product(pineapple)
order.add_product(lemon, 0.5)

print(order)
