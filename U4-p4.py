import os
def findfile(name,search):
    result = []

    for root,dir,files in os.walk(search):
        if name in files:
            result.append(os.path.join(root,name))

        if result == []:
            print("not found file")
        else:
            return result

fname=input("Enter File Create name :: ")
f=open(fname,'w')
f.close()
        
name= input("Enter File Name :: ")
print(findfile(name,os.getcwd()))
