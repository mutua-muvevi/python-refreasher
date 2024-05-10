age = int(input("What is your age : "))

if age < 0:
    print("That is an invalid age")
elif age > 200:
    print("Average humans arent supposed to get that old")
else:
    is_diabetic = str(input("Are your diabetic (True or False) : "))

    if is_diabetic == "True":
        print("You are not supposed to drink because you are diabetic")
    else:
        print("Let's party")
 