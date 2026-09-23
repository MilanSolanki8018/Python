# Search Position of Element in Array using INDEX()

import array as arr

a=arr.array('i',[10,20,30,40,50,60,70])
print(a)

x=int(input("Enter the Element of which you want to find Index : "))
if(x in a):
    print("\nIndex is :" ,a.index(x))
else:
    print("\nNot Found")
