name = "stringer"
name_with_digit = "Sky fall 2017"
lorem_ipsum = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the "
               "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type "
               "and scrambled it to make a type specimen book.")

# length
print(len(name))

# find
print(name.find("t"))

# replace
print(name.replace("er", "s"))

# upper case
print(name.upper())

# isdigit checks whether there a string is a digit
print("Does string the have digit : " + str(name_with_digit.isdigit()))

# isalpha checks if the string is alphabetical numbers
print("Is the string alphabetical : " + str(name.isalpha()))

# isalnum checks whether a string is alphanumeric
print("Is alphanumeric : " + str(name_with_digit.isalnum()))

# count: Counts the number of characters in a string
print("How many f's are there : ", lorem_ipsum.count("f"))

# print strings more than number of times
print(name * 3)