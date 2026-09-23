# BUBBLE-SORT AN ARRAY/LIST ELEMENTS

import array as arr
a=arr.array('i',[50,30,80,20,40,60,70,30])

def bubblesort(a):
    for i in range( 0, len(a)-1 ):            #length=8   so, length-1=7   so,  range(0,7)   but, 7 index not count
        for j in range(len(a)-1 ):

            if a[j]>a[j+1]:

                temp=a[j]                     #temp=a
                a[j]=a[j+1]                #a=b   
                a[j+1]=temp                   #b=temp

    return(a)

print("Original Array : " ,a)

print("Sorted Array : " ,bubblesort(a))
