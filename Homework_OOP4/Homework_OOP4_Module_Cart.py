import Homework_OOP4_Module_Customer
import Homework_OOP4_Module_Product


class Cart:

    def __init__(self, customer: Homework_OOP4_Module_Customer.Customer):
        self.customer = customer
        self.products = []
        self.quantities = []

    def add_product(self, product: Homework_OOP4_Module_Product.Product, quantity: float = 1):
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

        return f'{self.customer}\n{res}\nTotal: {self.total()} $'
