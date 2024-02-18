class Vehicle:
    numb_wheels = 4

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def __str__(self):
        return f"I drive {self.make} {self.model}. It runs on {self.fuel}."

daily = Vehicle("Subaru", "Crosstrek")
print(daily)


print(daily.numb_wheels)
