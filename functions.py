# emoji converter

emojis = {
	":)": "😊",
	":(": "😔",
	":D": "🤣"
}

sentence = input(">> ")


def emoji_converter(input_sentence):
	output = ""
	words = input_sentence.split(" ")
	
	for word in words:
		output += emojis.get(word, word) + " "
	
	return output


output = emoji_converter(sentence)
print(output)
