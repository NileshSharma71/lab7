n=input("Enter a sentence: ")
k=input("Enter the word: ")
#with using inbuilt function:
wc=n.count(k)
if wc>0:
    print(f"{k} exists in the sentence.")
    print(f"{k} occurs {wc} time(s) in the sentence.")
else:
    print(f"{k} does not exists in the sentence.")
#without usinng inbuilt function:
wc=0
for i in range(len(n)-len(k)+1):
    if n[i:i+len(k)]==k:
        wc+=1
if wc>0:
    print(f"{k} exists in the sentence.")
    print(f"{k} occurs {wc} time(s) in the sentence.")
else:
    print(f"{k} does not exists in the sentence.")