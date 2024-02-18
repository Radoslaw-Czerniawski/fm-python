names = ["Nina", "Max", "Jimmy"]

upper_names = [name.upper() for name in names]
print(upper_names)

range_list = list(range(4))
print(range_list)

print(list(range(1,5,2)))

print([num * num for num in range(6)])

print(tuple(("length", len(name)) for name in names))

print(
    "\n".join([f"The name is {name}" for name in names])
)
