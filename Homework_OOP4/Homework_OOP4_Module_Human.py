class Human:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    def __str__(self):
        return f'{self.surname} {self.name}'

