# DICTIONARY

dic={'NAME' : 'APURV' , 'AGE' : 26}
print(dic)

print(dic['NAME'])

print(dic['AGE'])

print(dic.get('AGE'))

dic['CITY']= 'SURAT'
print(dic)

del dic['CITY']
print(dic)


l1=['A','B','C']
l2=[11,22,33]

d=dict(zip(l1,l2))
print(d)

print(len(dic))
