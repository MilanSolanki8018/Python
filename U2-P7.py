# no repeat element in list 1 and display them in list 2

l1=[10,10,20,50,10,20,40,40,30,30]
l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)


l1 = [10, 10, 20, 50, 10, 20, 40, 40, 30, 30]
l2 = set(l1)

print(l2)


l1 = [10, 10, 20, 50, 10, 20, 40, 40, 30, 30]
l2 = dict.fromkeys(l1)

print(l2)
