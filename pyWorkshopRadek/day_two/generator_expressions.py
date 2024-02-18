gen_expression = (num * num for num in range(6))

print(gen_expression)

for value in gen_expression:
    print(value)

my_list = list(range(10))
print(my_list[::2])
