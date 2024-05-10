# while loop
name = str(input("What is you name : "))

while len(name) == 0:
    name = str(input("You haven't typed your name yet. What is you name : "))

print("Ofcourse your name is", name)


# A program that takes an integer from user and calculates its sum
integer = str(input("Enter your digit : "))
counter = 0
sum_of_digits = 0

while counter < len(integer):
    sum_of_digits += int(integer[counter])
    print(sum_of_digits)
    counter += 1

# password checker
password = str(input("Enter your password. It should be between 8 and 30 characters : "))
password_counter = 0

while password_counter < len(password):
    print(password + str(password_counter))
    password_counter += 1

# even number printer
last_number = int(input("What is the last number : "))
beginning_number = int(input("What is the beginning number : "))

while beginning_number <= last_number:
    if beginning_number % 2 == 0:
        beginning_number += 2

    else:
        beginning_number += 1

    print(beginning_number)


# print a triangle pattern in while loop
triangle_number = int(input("Enter the triangle number here : "))
triangle_symbol = str(input("Enter the symbol here : "))

counter = 0
nested_counter = 0

while counter <= triangle_number:
    while nested_counter <= counter:
        print(triangle_symbol * counter, end="")
        nested_counter += 1
    print()
    counter += 1

# print a multiplication table
multiple_number = int(input("Enter the multiple number here : "))
counter = 1

while counter <= multiple_number:
    nested_counter = 1

    while nested_counter <= counter:
        print(str(nested_counter * counter), " ", end="")
        nested_counter += 1
    print()
    counter += 1

# sum of natural numbers
number_range_end = int(input("Enter your last number : "))
sum_of_numbers = 0
counter = 0

while counter <= number_range_end:
    sum_of_numbers = sum_of_numbers + counter
    counter += 1

print(sum_of_numbers)

# guess the number 3 times trial
secret_number = 9
counter = 0
trials = 3

while counter < trials:
    user_number = int(input("Enter your number : "))
    counter += 1

    if user_number == secret_number:
        print("You are correct!")
        break

    elif counter == trials:
        print("You tried your best but failed")

    else:
        print("you are wrong please try again")

# build a small car engine game simulation if given wrong commands 10 times it quits
car_commands = ["start", "stop", "quit"]
your_command = str(input(">> ")).lower()
wrong_commands_maximum = 3
wrong_commands = 0

while True:
    if your_command not in car_commands:
        print("Wrong command!")
        
        wrong_commands += 1
        
        if wrong_commands == wrong_commands_maximum:
            print("Car is confused and damaged")
            break
            
        your_command = str(input(">> ")).lower()
    else:
        print(f">> car {your_command}")
        your_command = str(input(">> ")).lower()
        
        if your_command == "quit":
            print("You have quited and now we exit")
            break
            