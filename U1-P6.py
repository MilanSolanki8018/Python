# Display Memory Locations of 2 Variables, using id() function, compare their values & location, check that two objects are same or not.

a=20
b=20

print("ID of a is : ",id(a))
print("ID of b is : ",id(b))

if(a is b):
    print("both have same identity")
else:
    print("both have not same identity")

if(id(a)==id(b)):
    print("same")
else:
    print("no")

if(id(a)!=id(b)):
    print("No")
else:
    print("Same")
