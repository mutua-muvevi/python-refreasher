# break = terminates loops
# continue = skips
# pass = this skips a block

# break
# we only have 10 laptops a user want 100 laptops we want to sell 10 then break
# while loop
laptops_stock = 10
laptops_needed = int(input("How many laptops do you want to buy ? "))
counter = 1

while counter <= laptops_needed:
	if counter > laptops_stock:
		print("We have run out of stock dear customer")
		break

	print(str(counter), "Laptop(s) bought")
	counter += 1

# for loop
for i in range(laptops_needed):
	if i > laptops_stock:
		print("We have run out of stock dear customer")
		break

	print(str(i), "Laptop(s) bought")


# continue
# we want to print all number from 0 to 100 except all numbers divisible by 5

numbers = 20
counter = 1

# for loop
for i in range(numbers):
	if i % 5 == 0:
		continue

	print(i)

# while loop
while counter <= numbers:
	if counter % 5 == 0:
		counter += 1
		continue
	
	print(counter)
	counter += 1
