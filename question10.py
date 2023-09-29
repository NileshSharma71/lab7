n=input("Enter: ")
w=n.split("-")
for i in range(len(w)):
    for j in range(i+1,len(w)):
        if w[j] > w[j + 1]:
            w[j],w[j+1]=w[j+1],w[j]
fs="-".join(w)
print("Final ans.: ",fs)