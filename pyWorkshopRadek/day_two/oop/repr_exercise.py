import datetime
from initializer_methods import Car

now = datetime.datetime.now()

print(str(now))
print(repr(now))

car_instance = Car("Subaru")
print(str(car_instance))
print(repr(car_instance))
