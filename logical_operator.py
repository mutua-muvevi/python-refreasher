# logical operator (and, or, not)
body_temperature = int(input("What is your body temperature :"))
measure_unit = str(input("What is the unit measurement that you are using (C or K)"))
is_vision_blurry = str(input("Is you vision blurry (Yes or No) : "))
#
# # using "and" and "or"
if measure_unit == "K":
    body_temperature = body_temperature / 273.15
else:

    if body_temperature <= 20 or body_temperature >= 40:
        if body_temperature >= 40 and is_vision_blurry == "Yes":
            print("You have a fever and you need to see the doctor")
        elif body_temperature < 30 and is_vision_blurry == "Yes":
            print("You are almost dead")
    else:
        print("Human temp range")

# using "not"
language = str(input("What language do you speak : "))

if not (language == "English"):
    print("I can not understand You")
else :
    language_type = str(input("Is it American or Uk : "))
    if language_type == "Uk":
        print("Bloody Hell")
    else:
        print("What the fuck")
