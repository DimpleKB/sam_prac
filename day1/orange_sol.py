def partition(orange,low,high):
    if(low>=high):
        return 
    k=low
    pivot=orange[high]
    for i in range(low,high):
        if (orange[i]<=pivot):
            orange[i],orange[k]=orange[k],orange[i]
            k+=1
    orange[high],orange[k]=orange[k],orange[high]
    partition(orange,low,k-1)
    partition(orange,k+1,high)
n=int(input("enter number of oranges"))
orange=list(map(int,input().split()))
print(orange)
partition(orange,0,len(orange)-1)
print(orange)