my_set= {num * num for num in range(11)}
print(my_set)

my_dict = {i:val  for i, val in enumerate(my_set)}
print(my_dict)
