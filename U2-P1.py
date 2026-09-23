#Unit 2 : Program 1 : CREATE ONE ARRAY FROM ANOTHER ARRAY (SAME COPY)

a1=[1,2,3,4,5]
a2=[None]*len(a1)

for i in range(0,len(a1)):
    a2[i]=a1[i]

print("Elements of an Original Array : \n")
for i in a1:
    print(i)

print("Elements of the New Array : \n")
for i in range(0,len(a2)):
    print(a2[i])






