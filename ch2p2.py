#Create a program to retrive, display and update only a range of elements from an array usung indexing and slicing in array.
import array as arr
a=arr.array('i',[1,2,3,4,5,6,7]);
print(a)
#update array index 1
a[1]=10
print(a)
#update array using slicing
a[0:2]=arr.array('i',[9,8])
print(a)
