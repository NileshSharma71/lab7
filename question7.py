n=input("Enter: ")
uc=set()
rs=""
for char in n:
    if char not in uc:
        rs+=char
        uc.add(char)
print("string after removing duplicates: ",rs)