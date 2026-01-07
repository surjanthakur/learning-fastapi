class Phone:
    __counter = 1

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    @staticmethod
    def get_counter():
        print(Phone.__counter)

    @staticmethod
    def add_counter(count):
        if type(count) == int:
            Phone.__counter += count
            print("count added")


s1 = Phone("apple", 3000)
s2 = Phone("apple", 4000)

s1.add_counter(20)
s1.get_counter()

s2.get_counter()
