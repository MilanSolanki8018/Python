
try:
    a = eval(input("Enter a Divident :"))
    b = eval(input("Enter a devisior :"))
    ans=a/b
except (TypeError, SyntaxError):
    print("error")
else:
    print("Ans",ans)
