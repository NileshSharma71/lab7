k=[]
while True:
    n=int(input("Enter (1 to 10): "))
    if not(n>=1 and n<=10):
        break
    if n==-1:
        break
    k.append(n)
if not(n>=1 and n<=10):
    a=[1,2]
    b=[3,4]
    c=[5,6]
    d=[7,8]
    e=[9,10]
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    for i in k:
        for j in a:
            if j==i:
                c1+=1
        for w in b:
            if w==i:
                c2+=1
        for f in c:
            if f==i:
                c3+=1
        for o in d:
            if o==i:
                c4+=1
        for l in e:
            if l==i:
                c5+=1
    a1=(c1/len(k))*100
    a2=(c2/len(k))*100
    a3=(c3/len(k))*100
    a4=(c4/len(k))*100
    a5=(c5/len(k))*100
    a="#"
    print("1-2: ",a*int(a1%10),f"{a1:.2f}")
    print("3-4: ",a*int(a2%10),f"{a2:.2f}")
    print("5-6: ",a*int(a3%10),f"{a3:.2f}")
    print("7-8: ",a*int(a4%10),f"{a4:.2f}")
    print("9-10: ",a*int(a5%10),f"{a5:.2f}")

else:
    print("please enter number from 1 to 10!")