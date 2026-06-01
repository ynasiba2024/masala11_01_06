#11-masala
class House:
    def __init__(self, address, price):
        self.address = address
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, p):
        self.__price = p

h1 = House("Toshkent", 50000)

print(h1.price)

h1.price = 70000
print(h1.price)
