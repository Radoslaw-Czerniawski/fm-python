class Vehicle:
    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def is_eco_friendly(self):
        if self.fuel == "gas":
            return False
        else:
            return True

class Car(Vehicle):
    def __init__(self, make, model, fuel="gas", number_of_wheels=4):
        super().__init__(make, model, fuel)
        self.number_of_wheels = number_of_wheels

if __name__ == "__main__":
    print(f"Is bool a subclass of int: {issubclass(bool, int)}")

    four_by_four = Vehicle("zoom", "goes fast", fuel="cooking oil")
    print(four_by_four.fuel)
    print(four_by_four.is_eco_friendly())

    my_subaru = Car("subaru", "cross trek", fuel="diesel")
    print(my_subaru.number_of_wheels)
    print(my_subaru.is_eco_friendly())

