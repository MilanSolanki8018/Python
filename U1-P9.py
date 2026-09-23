# MENU-DRIVEN : AREA OF CIRCLE, TRIANGLE, SIMPLE INTEREST, QUIT, ERROR-MSG

def mm():

    print("1 : FIND AREA OF CIRCLE : ")
    print("2 : FIND AREA OF TRIANGLE : ")
    print("3 : FIND SIMPLE INTEREST : ")
    print("4 : QUIT ")
    ch=int(input("ENTER YOUR CHOICE : "))

    if ch==1:
       r=float(input("ENTER THE RADIUS OF CIRCLE : "))
       area=3.14*r*r
       print("AREA OF CIRCLE IS : %.2f" %area)
       print()
       mm()

    elif ch==2:
        b=float(input("ENTER THE BASE OF TRIANGLE : "))
        h=float(input("ENTER THE HEIGHT OF TRIANGLE : "))
        area=b*h/2
        print("AREA OF TRIANGLE IS : %.2f" %area)
        print()
        mm()

    elif ch==3:
        p=float(input("ENTER THE PRINCIPLE AMOUNT : "))
        r=float(input("ENTER THE RATE : "))
        n=float(input("ENTER THE TIME IN 'YEARS' : "))
        i=p*r*n/100
        print(f"SIMPLE INTEREST WILL BE : {i}" )
        print()
        mm()
      
            
    elif ch==4:
        exit

    else:
        print("I N V A L I D  C H O I C E !! \nT R Y  A G A I N !")
        print()
        mm()

mm()
            


