# there are two ways to name slice a string
# 1. string[start:stop:step]
# 2. slice(start,stop,step)

fullname = "Joseph Sammy"

first_name = fullname.split()[0]
last_name = fullname.split()[1]

# indexing operator
reversed_string = fullname[::-1]

print("Your fullname is", first_name , last_name)
print(fullname[0:10:2])
print(reversed_string)

# slice
website_url = "https://mail.google.com"

slicer = slice(8, -4)

print(website_url[slicer])
