my_nums = [num * num for num in range(8)]

# add only even numbers to array (0 is even)
even_squares = [num for num in my_nums if num % 2 == 0]
print(
    ", ".join([str(even_square) for even_square in even_squares])
)

sum_of_numbers = sum(even_squares)
print(sum_of_numbers)

print(min(even_squares))
print(max(even_squares))

even_squares.sort(reverse=True)
print(even_squares)

lottery_numbers = [numb.strip() for numb in "4, 5, 134, 10".split(",")]
print(lottery_numbers)
