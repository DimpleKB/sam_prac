#using string type
# num=int(input("enter  a number"))
# strnum=str(num)
# sum=0
# j=1
# for i in range(len(strnum)):
#     if j%2!=0:
#         if int(strnum[i])%2==0:
#             sum+=int(strnum[i])
#     j+=1
# print(sum)

#without using string
num=int(input("enter  a  number"))
flip=1
sum=0
while(num>0):
    if flip==1 and (num%10)%2==0:
        sum+=num%10
    num//=10
    flip=not flip
print(sum)
    