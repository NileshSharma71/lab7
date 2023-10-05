n=input("Enter: ")
n=n.split("-")
a=[]
i=0
while i<=(len(n)):
    x=min(n)
    a.append(x)
    n.remove(x)
    i+=1
print("-".join(a))