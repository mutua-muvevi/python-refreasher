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

# # even number printer
last_number = int(input("What is the last number : "))
beginning_number = int(input("What is the beginning number : "))

while beginning_number <= last_number:
    if beginning_number % 2 == 0:
        beginning_number += 2

    else:
        beginning_number += 1

    print(beginning_number)

