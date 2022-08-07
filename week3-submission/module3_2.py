"""define a class"""

class Car:
    """create attributes of the class"""
    name = "Toyota"
    size = 200
    color = "Blue"
    price = 50000
    producer = "Mariam Ade"

    """define the class methods"""
    def get_name(self, name):
        self.name = name
        print(self.name)

    def get_size(self, size):
        self.size = size
        print(self.size)

    def get_color(self, color):
        self.color = color
        print(self.color)

    def get_price(self, price):
        self.price = price
        print(self.price)

    def get_producer(self, producer):
        self.producer = producer
        print(self.producer)

# create an instance of the class
car = Car()

# call the object methods
print(car.name)
print(car.size)
print(car.color)
print(car.price)
print(car.producer)
