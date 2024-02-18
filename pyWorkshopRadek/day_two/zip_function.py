my_dict = {num: num*num for num in range(11)}
print(my_dict)

players = ("Nina", "Bob", "Alice")
scores = (100, 5, 97)

print(list(zip(players,scores)))

# print({key:value for key, value in zip(players, scores)})
print(dict(zip(players, scores)))
