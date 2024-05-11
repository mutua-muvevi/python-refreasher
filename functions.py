import math


# # emoji converter
#
# emojis = {
# 	":)": "😊",
# 	":(": "😔",
# 	":D": "🤣"
# }
#
# sentence = input(">> ")
#
#
# def emoji_converter(input_sentence):
# 	output = ""
# 	words = input_sentence.split(" ")
#
# 	for word in words:
# 		output += emojis.get(word, word) + " "
#
# 	return output
#
#
# output = emoji_converter(sentence)
# print(output)

# # a function that creates user object for you
# user_object = {}
#
# name = input("What is your name : ")
# age = int(input("What is your age : "))
# profession = input("What is your profession : ")
#
#
# # creates turple when you do it this way
# def create_user(name, age, profession):
# 	user_object[name, profession, age] = name, profession, age
#
# 	return user_object
#
#
# new_user = create_user(name, age, profession)
# print((new_user))
#
#
# for keys, value in new_user.items():
# 	print("Keys", keys, type(keys))
# 	print("Values", value)

# key word arguments
def calculate_area(radius, units):
	area = math.pi * pow(radius, 2)
	return area, units


area_circle = calculate_area(units="metres", radius=int(input("Enter the radius")))
print(area_circle)
print(type(area_circle))