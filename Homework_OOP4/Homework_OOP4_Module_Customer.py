class Customer:

    def __init__(self, surname, name, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f'{self.surname} {self.name}; {self.phone_number}'
