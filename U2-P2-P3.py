
# ARRAY & LIST - display, slicing, update, append, insert, pop, remove, index, count, tolist



from array import*          #or             #import array as arr    then    a=arr.array('i',[10,20,30,40,50,60])


a=array('i',[10,20,30,40,50,60])
print(a)                                    #array('i',[10,20,30,40,50,60])     #DISPLAY           #if remove ('i',........)   then   output : array.array[10,20,30,40,50,60]


print(a[:])                                 #array('i',[10,20,30,40,50,60])     #FULL DISPLAY
print(a[2])                                 #30                                 #SPECIFIC DISPLAY


print(a[2:5])                               #30,40,50                           #SLICING
print(a[2:])                                #30,40,50,60                        # 2nd index : TO END
print(a[:3])                                #10,20,30                           # START TO : till 3rd index

a.append(77)
print(a)                                    #10,20,30,40,50,60,77               #add new value at last

a.insert(2,88)
print(a)                                    #10,20,88,30,40,50,60,77            #add value at index(position)

a.pop(4)
print(a)                                    #10,20,88,30,50,60,77               #delete value by index(position)

a.remove(77)
print(a)                                    #10,20,88,30,50,60                  #delete value directly

print(a.count(20))                          #1                                  #count value how many times appears
print(a.index(10))                          #0                                  #show index(position) of value
print(a.tolist())                           #[10,20,88,30,50,60]                #show array as list


a[5]=99
print(a)

a[0:2]=array('i',[300,400])
print(a)


R1=[11,22,33]
print(R1)

repeat=(R1*2)
print(repeat)

repeat2=[i for i in R1 for _ in range(2)]
print(repeat2)



