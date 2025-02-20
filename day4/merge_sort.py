''' best,average and worst case efficieny (time complexity) is o(nlogn)
    it is also called as stable sorting technique'''


#using 2 array left and right in the merge function
def merge(numbers,low,mid,high):
    left=numbers[low:mid+1]
    right=numbers[mid+1:high+1]
    k=low
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            numbers[k]=left[i]
            i+=1
        elif left[i]>right[j]:
            numbers[k]=right[j]
            j+=1
        else:
            numbers[k]=left[i]
            i+=1
        k+=1
    # while i < len(left):
    #     numbers[k]=left[i]
    #     i+=1
    #     k+=1
    # while j < len(right):
    #     numbers[k]=right[j]
    #     j+=1
    #     k+=1

    numbers[k:high+1] = left[i:]+right[j:]
    
def merge_sort(numbers,low,high):
    if low< high:
        mid=(low+high)//2
        merge_sort(numbers,low,mid)
        merge_sort(numbers,mid+1,high)
        merge(numbers,low,mid,high)
numbers=[5,4,3,2,1,1,6,3,7,8]
merge_sort(numbers,0,len(numbers)-1)
print(numbers)

#using only one array (merged_array)
# def merge(numbers,low,mid,high):
#     i=low
#     j=mid+1
#     merged_array=[]
#     while i<=mid and j<=high:
#         if numbers[i]<numbers[j]:
#             merged_array.append(numbers[i])
#             i+=1
#         elif numbers[i]>numbers[j]:
#             merged_array.append(numbers[j])     
#             j+=1
#         else:
#             merged_array.append(numbers[i])
#             i+=1
#     while i <= mid:
#         merged_array.append(numbers[i])
#         i+=1
#     while j <=high:
#         merged_array.append(numbers[j])
#         j+=1
#     j=0
#     for i in range(low,high+1):
#         numbers[i]=merged_array[j]
#         j+=1
    
# def merge_sort(numbers,low,high):
#     if low< high:
#         mid=(low+high)//2
#         merge_sort(numbers,low,mid)
#         merge_sort(numbers,mid+1,high)
#         merge(numbers,low,mid,high)
# numbers=[5,4,3,2,1,1,2,90,67,11,0]
# merge_sort(numbers,0,len(numbers)-1)
# print(numbers)