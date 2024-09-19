#6. Write a program to generate prime number with the help of a function to test prime or not.

def test_prime(num):
    if num>1:
        for i in range(2,num):
            if(num%i) == 0:
                print(num,"is not a prime number")
                break
            else:
                print(num,"is prime number")
                break
    else:
        print(num,"is not prime number")
    
num=int(input("Enter number to check prime or not :: "))
test_prime(num)
