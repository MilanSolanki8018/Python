a = int(input("Enter a Divident :"))
b = int(input("Enter a devisior :"))

try:
    ans=a/b
except ZeroDivitionError:
    print("zero divition error")
else:
    print("Ans",ans)
