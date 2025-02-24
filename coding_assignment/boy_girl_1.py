t=int(input('enter number of test cases'))
while(t>0):
    n=int(input("enter number of boys and girls"))
    b=[]
    g=[]
    for i in range(n):
        h=int(input(f"enter height of boy {i+1} : "))
        b.append(h)
    for i in range(n):
        h=int(input(f"enter height of girl {i+1} : "))
        g.append(h)
    b.sort()
    g.sort()
    sort=[]
    i=0
    j=0
    k=0
    while i<n and j<n:
        if b[i]<g[j]:
            sort.append(b[i])
            i+=1
            k+=1
        else :
            sort.append(g[j])
            j+=1   
            k+=1
        
    while i<n:
        sort.append(b[i])
        i+=1
    while j<n:
        sort.append(g[j])
        j+=1
    print(sort)
    flag=0
    for k in range(1,len(sort)):
        if (sort[k-1] in b and sort[k-1] in g) or (sort[k] in b and sort[k] in g):
            continue
        if (sort[k-1] in b and sort[k] in b and sort[k-1]!=sort[k]) or (sort[k-1] in g and sort[k]in g and sort[k-1]!=sort[k]):
            print("no")
            flag=1
            break
    if flag==0:
        print("yes")
    t-=1