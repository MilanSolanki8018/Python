
min=int(input("Enter the Minimum Value : "))
max=int(input("Enter the Maximum Value : "))
even_total=0
odd_total=0

for n in range(min,max+1):
    if(n%2==0):
            even_total+=n
    else:
            odd_total+=n

print(max+1)
print(f"the sum of even numbers from {min} to {max} = {even_total}")
print("the sum of odd numbers from {0} to {1} = {2}".format(min,max,odd_total))


#sys.argv[]



               
