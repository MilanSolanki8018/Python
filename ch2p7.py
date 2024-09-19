# 7.Write a python program that removes any repeated items from a list so that each item appers at most once. For instance, the list [1,2,2,3,4,4,4] Would Become [1,2,3,4].

list1=[1,1,2,3,3,3,4,4,5,5,5,5,0]
list2=[1]

for i in list1:
   if i not in list2:
       list2.append(i)
print(list2)
