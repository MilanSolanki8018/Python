import datetime
year=int(input("Enter Year :"))
month=int(input("Enter Month :"))
day=int(input("Enter Day :"))
print(year,'-',month,'-',day)

birthday=datetime.datetime.now()
diff = now-birtday
print("diffrence is :",diff.days)
