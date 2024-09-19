#9. Write a program to demonstrate the use of positional argument keyword argument and default arguments.

def positional(dhaval,raj,manoj):
    print(dhaval,raj,manoj)
a='dhaval'
b='raj'
c='manoj'

def keyword(dhaval,raj,manoj):
    print(dhaval,raj,manoj)
a='dhaval'
b='raj'
c='manoj'

def defults(dhaval,raj,manoj='mihir'):
    print(dhaval,raj,manoj)
a='dhaval'
b='raj'


positional(a,b,c)
keyword(dhaval=a,raj=b,manoj=c)
defults(dhaval=a,raj=b)
