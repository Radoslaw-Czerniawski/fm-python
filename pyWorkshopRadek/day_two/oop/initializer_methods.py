class Car:
    runs = True
    number_of_wheels = 4

    def __init__(self, name):
        self.name = name
        print(f"New Car {self.name} was created")

    def __str__(self):
        return f"My car the {self.name} currently {self.runs}"

    def __repr__(self):
        return f"Car({self.name})"

    def start(self):
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken")

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels


if __name__ == "__main__":
    new_car = Car("Subaru")

    print(Car.get_number_of_wheels())

    print(type(new_car))
    print(isinstance(42, int))
    print(isinstance(new_car, Car))

    # don't use this in production code
    print(isinstance(True, int)) # True

    # booleans were later added after integers so they are subclasses of int
    print(True + True) # 2 XDD

    print(any([False, True, True, False])) # True
    print(all([False, True, True, False])) # False
