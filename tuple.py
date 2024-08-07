tup=(34,12,67,'Rohit',13)

#Converting a list into tuple using tuple function

'''List =[7,8,9]
tp= tuple(List)
print(tp)'''

#Create a tuple using Range()

'''tp= tuple(range(0,21,2))
print(tp)'''

#Slicing Tuple

'''print(tup)
print(tup[2])
print(tup[2:4])
print(tup[-2])
print(tup[-1:-6:-2])'''

#Basic Operation in tuple

'''a = (1,2,3,"Dhaval")
b = (7,8,9,6)

print(len(a))
print(a+b)
print(b*2)
val= 30
print(val in a)
print(max(b))
print(a.count(2))
print(b.index(9))
print(sorted(b))'''

#Nested Tuple

'''one =(("Raj","C++",34),("Dipak","Python",96),("Dhaval","Java",76))
for i in one:
    print(i)'''

#Sorting Tuple

one = [(1,('a')),(3,('c')),(9,('e')),(5,('z'))]
tp = sorted(one)
print (tp)
tp = sorted(one, reverse=True)
print (tp)
