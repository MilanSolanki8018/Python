#3.Write a program to understand various methods of array class mentioned: append, insert, pop, remove,index, tolist and count.

a=[1,2,3,4,5,6,7]
print(a)
#insert at last
a.append(10)
print(a)
#insert by position
a.insert(1,1.5)
print(a)
#remove by value
a.remove(1.5)
print(a)
#remove by index
a.pop(6)
print(a)
#print by index
print(a.index(5)) #a[2]
print(a.count(4))

#import numpy as np
#arr = np.array([1, 2, 3, 4, 5])
#print(a.tolist())


