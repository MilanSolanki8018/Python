# 10 write a program to assert the user enters a number greater than zero.

num =int( input('Enter Number  ::'))
assert num>=0, "Only positive number accepted."
print("your entered : ", num)
