username = input("Enter your username: ")
password = input("Enter your password: ")
len = len(password)
print(type(len))
print(len)
if len < 6:
    check = "weak"
elif len >= 6 and len < 10:
    check = "medium"
else:
    check = "strong"

print("Your password is " + check + ".")