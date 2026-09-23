#Swap Number Without Tempoary Variable.

a=int(input("Enter the First Number : "))
b=int(input("Enter the Second Number : "))


a=a+b
b=a-b
a=a-b

print("After Swapping a is :",a, "& b is :",b)

x=int(input("Enter"))
y=int(input("Enter "))

x,y=y,x
print(x,y)
