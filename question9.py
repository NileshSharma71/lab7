n=input("Enter(in capitals): ")
k=[]
count=0
for i in range(65,91):
    op=chr(i)
    k.append(op)

for kj in k:
    if kj in n:
        count+=1
if count==26:
    print("The string is pangram.")
else:
    print("The string is not pangram.")