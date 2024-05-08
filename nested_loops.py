# nested loops

# build a rectangle
rows = int(input("Enter the number of rows : "))
columns = int(input("Enter the number of columns : "))
fill_symbol = str(input("Enter the your fill symbol : "))

# draw a rectangle
for i in range(rows):
    print("> ", end="")
    for j in range(columns):
        print(fill_symbol, end="")
    print(" <")

# draw a square
square_rows = int(input("Enter the number of square rows : "))
square_columns = int(input("Enter the number of square columns : "))
fill_symbol = str(input("Enter the your fill symbol : "))

for i in range(square_rows):
    for j in range(square_columns):
        print(fill_symbol, end="")
    print()

# print a multiplication table
mult_rows = int(input("Enter the rows range : "))
mult_columns = int(input("Enter the columns range : "))

for i in range(1, mult_rows + 1):
    print()
    for j in range(1, mult_columns + 1):
        print(str(j * i) + " ", end="")


# print a triangle pattern
triangle_number = int(input("Enter the triangle number here : "))
triangle_symbol = str(input("Enter the symbol here : "))

for i in range(1, triangle_number + 1):
    for j in range(i):
        print(triangle_symbol, end="")
    print()

# print a number pattern
number_max = int(input("Enter the number here : "))

for i in range(1, number_max + 1):
    print()
    for j in range(1, i + 1):
        print(j, end="")

# print a pascal number
pascal_number = int(input("Enter the number of rows for Pascal's triangle: "))

for i in range(pascal_number):
    coefficient = 1
    for j in range(1, pascal_number - i + 1):
        print("+", end="")

    for k in range(0, i + 1):
        print(coefficient, end=" ")
        coefficient = coefficient * (i - k) // (k + 1)

    print()


