from datetime import datetime

#t=datetime.today()
#print(t)

print("TODAY IS : " ,datetime.today().strftime("%y-%m-%d"))

b=datetime(2005,9,4)


print("GAPE : " ,(datetime.today()-b).days)
