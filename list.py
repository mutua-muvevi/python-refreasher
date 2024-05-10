# list it's just like arrays in javascript
foods = ["ugali", "chapati", "rice", "chipo"]
matrix = [[1, 2], [3, 4]]
matrix_3d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
iterable_list = list(range(1, 20 + 1))

countries = [
	"algeria", "angola", "benin", "botswana", "burkina faso",
	"burundi", "cabo verde", "cameroon", "central african republic",
	"chad", "comoros", "democratic republic of the congo",
	"republic of the congo", "djibouti", "egypt", "equatorial guinea",
	"eritrea", "eswatini", "ethiopia", "gabon", "gambia", "ghana",
	"guinea", "guinea-bissau", "ivory coast", "kenya",
	"lesotho", "liberia", "libya", "madagascar", "malawi", "mali",
	"mauritania", "mauritius", "morocco", "mozambique", "namibia",
	"niger", "nigeria", "rwanda", "sao tome and principe", "senegal",
	"seychelles", "sierra leone", "somalia", "south africa",
	"south sudan", "sudan", "tanzania", "togo", "tunisia", "uganda",
	"western sahara", "zambia", "zimbabwe"
]


print(iterable_list)

# if chipo is in the array it should print not healthy
for i in foods:
	if i == "chipo":
		print("Unhealthy food detected", i)

# change the beginning on every string to uppercase
for i in range(len(foods)):
	foods[i] = foods[i].capitalize()
print(foods)

# while loop
counter = 0

print(foods)

# slicing an index
# slicing list return new list it doesn't affect the original one [start:end:step]
sliced_list = foods[0:3]
print(sliced_list)


# given a beginning and last number print every number in an increment of 3
numbers = list(range(int(input("Enter the number here : "))))
end_number = int(input("Enter the last number : "))
plus_3 = numbers[:end_number:3]
print(plus_3)

# list unpacking
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
first, second, third = numbers[0], numbers[1], numbers[2]

# if we only want to unpack two
first_num, second_num, *others, last = numbers


while counter < len(foods):
	foods[counter] = foods[counter].capitalize()
print(first_num, second_num, others, last)


for i in enumerate(numbers):
	print(i)


# loop through list of countries and add ea countries to africa_mashariki in uppercase
africa_mashariki = []

for i in countries:
	if i in ["kenya", "uganda", "tanzania", "rwanda", "burundi"]:
		i = i.capitalize()
		africa_mashariki.append(i)

print(africa_mashariki)

# while loop to do the above
counter = 0

while counter < len(countries):
	if countries[counter] in ["kenya", "uganda", "tanzania", "rwanda", "burundi"]:
		countries[counter] = countries[counter].capitalize()
		africa_mashariki.append(countries[counter])
	counter += 1

print(africa_mashariki)

# a program that prints the largest number in a list
numbers_in_a_list = [10, 12, 3, 4, 5, 6]
numbers_in_a_list.sort()

largest_number = numbers_in_a_list[-1]
print(largest_number)
