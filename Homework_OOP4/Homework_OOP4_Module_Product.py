class Product:

    def __init__(self, product, description, dimensions, price):
        self.product = product
        self.description = description
        self.dimensions = dimensions
        self.price = price

    def __str__(self):
        return f'{self.product} {self.description},{self.dimensions}: {self.price}'
