abc=[11,22,33,44,55]
print(abc)

abc.append(66)
print(abc)

abc.insert(0,99)
print(abc)

d=abc.copy()
print(d)

pqr=['A','B','C',33]

abc.extend(pqr)
print(abc)

print(abc.count(33))

abc.remove('C')
print(abc)


pqr.pop(1)
print(pqr)

print(pqr.pop())


pqr.sort()
print(pqr)
 
