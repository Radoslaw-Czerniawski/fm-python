class EmptyInputException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

name = input("Hello human, what is you name?: ")

if name.strip() == "":
    raise EmptyInputException("Input cannot be empty!")

print(f"Hello, {name}, nice to meet you!")

