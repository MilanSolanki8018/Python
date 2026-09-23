class Parent:

    def __init__(self,n):
        self.name=n
    def display(self):
        print(self.name)
        print("HELLO PARENT")

class Child(Parent):

    def __init__(self,n):
        super().__init__(n)
    def display(self):
        super().display()
        print("HELLO CHILD")
x=Child("WELCOME")
x.display()
