import time

# for loop
username = str(input("What is your username : "))
vowel_counter = 0

for i in range(len(username)):
    if username[i] in "aeiou":
        print(username[i] == "a")
        vowel_counter += 1

print("The number of vowels here is", str(vowel_counter))

# triangle printer
for i in range(5):
    print("*" * i)

# replace some value in a given str with users value
user_string = str(input("Enter your string here : "))
what_to_replace = str(input("What do you want to replace : "))
replacer = str(input("What is your replacer : "))

for i in user_string:
    user_string = user_string.replace(what_to_replace, replacer)

print("Your final string", user_string)

# even number printer
start_number = int(input("Your starting number : "))
last_number = int(input("Your last number : "))
even_numbers = []

for i in range(start_number, last_number):
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)


# countdown timer
number_of_seconds = int(input("Enter your start time : "))

for seconds in range(number_of_seconds, 0, -1):
    print(seconds)
    time.sleep(1)
print("Explode BOOOOOM")


# numbers divisible by 7
number_range_start = int(input("Enter your first number : "))
number_range_end = int(input("Enter your last number : "))

for i in range(number_range_start, number_range_end):
    if i % 7 == 0:
        print(str(i), ", ", end="")

# sum of natural numbers
number_range_start = int(input("Enter your first number : "))
number_range_end = int(input("Enter your last number : "))
sum_of_numbers = 0

for i in range(number_range_start, number_range_end + 1):
    sum_of_numbers += i
print(sum_of_numbers)

# in a range if number is divisible by 5 print divisible by 5
start_range = int(input("Enter the beginning number : "))
end_range = int(input("Enter the end number : "))

for i in range(start_range, end_range + 1):
    if i % 5 == 0:
        print("divisible by 5")
    else:
        print(i)