# age = int(input("What is your age : "))
#
# if age < 0:
#     print("That is an invalid age")
# elif age > 200:
#     print("Average humans arent supposed to get that old")
# else:
#     is_diabetic = str(input("Are your diabetic (True or False) : "))
#
#     if is_diabetic == "True":
#         print("You are not supposed to drink because you are diabetic")
#     else:
#         print("Let's party")
#

# weight converter
weight = float(input("What is your weight : "))
unit_of_measurement = str(input("Is in K (kilograms) or L(pounds) : "))

if unit_of_measurement == "K" or unit_of_measurement == "k":
    weight = weight * 2.20462
    unit_of_measurement = "pounds"
else:
    weight = weight / 0.453592
    unit_of_measurement = "kilograms"

print(f"Your weight is {str(weight)} {unit_of_measurement}")
