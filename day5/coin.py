num=int(input("enter rupees"))
coin=[5,10,15,20,25]
cnt=0
for i in range(len(coin)):
    for j in range(len(coin)-i-1):
        if coin[j]<coin[j+1]:
            coin[j],coin[j+1]=coin[j+1],coin[j]
d={}
print(coin)
for i in coin:
    n=num//i
    print(i,"=",n)
    num=num%i