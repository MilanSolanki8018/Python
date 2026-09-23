# STUDENT CLASS,    DATA MEMBERS(VARIABLES),    FUNCTIONS(METHODS),     OBJECT,     CALL

class Student:

    def __init__(self):

        self.name="APURV"
        self.age=24
        self.marks=75

    def display(self):

        print("NAME : " ,self.name)
        print("AGE : " ,self.age)
        print("MARKS : " ,self.marks)

s=Student()
s.display()


print()
# with constructor - having more than one parameters and default arguments


class Student1:

    def __init__(self, n='.', a=20, m=0):

        self.name=n
        self.age=a
        self.marks=m

    def display(self):

        print("NAME : " ,self.name)
        print("AGE : " ,self.age)
        print("MARKS : " ,self.marks)

x=Student1("APURV",24,75)
x.display()

y=Student1("DEV")
y.display()
    
