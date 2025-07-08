class car:#class
    def __init__(self, color, brand, price):
        self.color = color
        self.brand = brand
        self.price = price
    def change_color(self, color):
        self.color = color

benz = car('white', 'benz', 30000000) #object
print(benz.color)
print(benz.brand)
print(benz.price)

print(type(3))

benz.change_color('red')
print(benz.color)