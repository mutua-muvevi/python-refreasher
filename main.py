import functions
from functions import emoji_converter
from functions import find_max

# functions.calculate_area(50, units="metres")
output = emoji_converter("I am very happy today :) :) :) that is why i am laughing :D :D :D")
print(output)

list_of_numbers = [210, 15, 45, 96, 78, 69, 96, 103]
max_number = find_max(list_of_numbers)

print(max_number)