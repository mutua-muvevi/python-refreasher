customer = {
	"name": "user254",
	"age": 23,
	"gender": "male"
}

customer["profession"] = "software developer"
print(customer)


# create a method that stores user dictionary email, password, username, country
user = {}
keys = ["username", "email", "password", "country"]

for key in keys:
	user[key] = str(input(f"What is your {key}: "))

# let's ensure that the password does not include username
if user["password"] in user["username"]:
	print("Password should not contain characters of username")
	password = str(input("Repeat your password again"))

	user["password"] = password

print(user)

# a program that checks if all key values characters are greater than 3
for key, value in user.items():
	if key:
		print(key, value)
		user[key] = str(input(f"Please repeat the {key} again, and ensure characters are longer than 3"))


print(user)

# Emoji converter
emojis = {
	":)": "😊",
	":(": "😔",
}

sentence = input(">> ")
words = sentence.split(" ")

for word in words:
	if word in emojis.keys():
		print("The word", emojis[word])