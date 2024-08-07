Std = [556,"Rudra",84,96,75]
Xyz = [23,12,"Yash",45,14]

#Slicing List

'''print(Std)
print(Std[0])
print(Std[0:3])
print(Std[3:])
print(Std[:4])
print(Std[:])
print(Std[-2])
print(Std[-1:-5:-2])'''

#Looping in List
'''for i in Std:
    print(i)'''

#Update and Deleting List

'''Std.append(78)
print(Std)

Std.pop(3)
print(Std)

del Std[1]
print(Std)

Std.remove(556)  # Using Value
print(Std)'''


#Concatention Of Two List

'print(Std + Xyz)'

#Repetition Of Lists

'print(Std * 2)'

#Membership in List

'''a=556
print(a in Std)
print(a in Xyz)

b=12
print(b not in Std)
print(b not in Xyz)'''

#Aliasing List

'''Abc = Xyz
print(Xyz)
print(Abc)
Xyz[3]=34
print(Xyz)
print(Abc)''' 

#Cloning List

'''Abc = Xyz[:]
print(Xyz) # Xyz Is Cloned as Abc
print(Abc)
Xyz[3]=34
print(Xyz)
print(Abc)'''

#Nested List

a = [1,2,3]
b = [5,6,a]

print(b)
print(b[0])
print(b[2])
print(b[2][1])
print(b[2][2])

for i in b[2]:
   print(i)


