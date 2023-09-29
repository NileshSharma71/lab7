n=input("Enter: ")
cd=0
ca=0
csc=0
cua=0
cla=0
for i in n:
    if n.isdigit()==True:
        cd+=1
    if n.isalpha()==True:
        ca+=1
        if n.isupper()==True:
            pass






print("Total number of digits in the string.",cd)