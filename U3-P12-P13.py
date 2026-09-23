

# SINGLE INHERITANCE 1 SUPERCLASS AND 2 SUBCLASS

class Bank(object):                  #object is superclass for Bank Class

    cash=1000000
    @classmethod
    
    def chk(cls):
        print(cls.cash)

class Bank2(Bank):
    pass

class Bank3(Bank):

    cash=200000
    @classmethod

    def chk(cls):
        print(cls.cash+Bank.cash)

x=Bank2()
x.chk()

y=Bank3()
y.chk()


# MULTIPLE INHERITANCE : TWO BASE CLASS
print()

class Father:
    def height(self):
        print("Height is 6 feet")

class Mother:
    def skintone(self):
        print("Skintone is White")

class Child(Father,Mother):
    pass

c=Child()
print("Child inherited qualitie : ")
c.height()
c.skintone()
