n=input("Enter: ")
cd=0
ca=0
csc=0
cua=0
cla=0
for char in n:
    if char.isdigit():
        cd+=1
    if char.isalpha():
        ca+=1
        if char.isupper():
            cua+=1
        else:
            cla+=1
    if char.isalnum()==False:
        csc+=1
print("Total number of digits in the string.",cd)
print("Total number of alphabets in the string.",ca)
print("Total number of upper case alphabets in the string.",cua)
print("Total number of lower case alphabets in the string.",cla)
print("Total number of special characters in the string.",csc)