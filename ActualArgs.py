#Actual Args

#1. Positional Args

'''def name(m1,m2):  *Formal Args
     print("Tc",m1+m2)

name("Night ","Good")  *Actual Args
name("Good ","Night")'''

#Keyword Args

'''def Product(name,price):
     print("Product name :: ",name)
     print("Product price ::",price)

Product(name="Apple",price=100)
Product(price=200,name="Mango")'''

#Defualt Args

'''def Product(name,price=300):
     print("Product name :: ",name)
     print("Product price ::",price)

Product(name="Apple",price=100)
Product(name="Mango")'''

#Veriable Length Args

def Add(farg,*args):
     sum=0
     for i in args:
         sum +=i
     print("Sum is :: ", sum +farg)

Add(2)
Add(2,4)
Add(2,4,6)
Add(2,4,6,8)
