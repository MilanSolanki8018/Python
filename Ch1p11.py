#11. Write A program to serach an element in the list using for loop and also demonstrate the use of
#"else"with for loop.

list = [1,2,'What',4,'ccc',6]
n= 'python'

def search(list,n):
     for i in range(len(list)):
         if list[i] == n:
             return true

if search(list, n):
      print("found")
else:
     print("Not Found")
