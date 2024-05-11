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

# a function that creates user object for you
user_object = {}

name = input("What is your name : ")
age = int(input("What is your age : "))
profession = input("What is your profession : ")


def create_user(name, age, profession):
	user_object[name] = name
	user_object[profession] = profession
	user_object[age] = profession
	
	return user_object


new_user = create_user(name, age, profession)
print(new_user)
