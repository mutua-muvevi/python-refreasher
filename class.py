# class Animal:
# 	def eat(self):
# 		print("Eat")
#
# 	def reproduce(self):
# 		print("reproduce")
#
# human = Animal()
# human.eat()
#
# human.ref = {
# 	"age" : "25",
# 	"name" : "Jose",
# 	"profession" : "software developer"
# }
#
# print(human.ref)

# class Point:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
#
#
# point = Point(10, 20)
# print(point.x, point.y)

# class Person:
# 	def __init__(self, name):
# 		self.name = name
#
# 	def talk(self):
# 		print("I do talk")
#
#
# person_one = Person("Jose")
# print(person_one.name)

# inheritance
class Mammals:
	def walk(self):
		print("walk")
	
	def run(self):
		print("run")
		
	def eat(self):
		print("eat")


class Humans(Mammals):
	def code(self):
		print("CODE")


human = Humans()
human.walk()
human.code()