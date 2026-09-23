# Generate Prime Numbers with help Function to test Prime or Not

def pn():

    x=int(input("Enter Number to Check : "))

    if(x>1):
        for i in range(2,x):
               if(x%i)==0:
                print("NO")
                pn()
            
        else:
            print("Yes")
            pn()

    else:
        print("error")
        pn()
pn()
