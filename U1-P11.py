# PROGRAM 11 : SEARCH ELEMENT USING FOR LOOP & DEMONSTRATE USE OF "ELSE" WITH FOR LOOP

def serch(a,list):
    for i in range(len(list)):
        if a==list[i]:
            return 1
        
list =[1,2,3,'c++',8]

a=5
if serch(a,list):
    print("found")
else:
    print("Not Found")
