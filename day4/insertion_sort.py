''' best efficieny of insertion sort is o(n)
    average and worst efficiency is o(n^2)
    it fails when the input size if large 
    it is used efficiently when we know that the array is already sorted or partially sorted or the input size is small
'''
'''pseudocode:
        from 2nd element to last element:
            copy current element into element
            j=index of element-1
            i=index of last element in sorted array
            while j>=0 and element<current element in sorted array:
                sorted_orray[j+1]=sorted_array[j]
                j--
            sorted_array[j+1]=element
        for i in range(1,len(arrat)):
            j=i-1;
            element=arrat[i]
            while j>=0 and element<array[j]:
                array[j+1]=array[j]
                j--
            array[j+1]=element
            '''

#program for list of integers
# lst=[5,4,3,2,1]
# for i in range(1,len(lst)):
#     temp=lst[i]
#     j=i-1
#     while j>=0 and temp < lst[j]:
#         lst[j+1]=lst[j]
#         j-=1
#     lst[j+1]=temp
# print(lst)


#program for string 
# lst="cbaABC"
# lst=lst.upper()
# for i in range(1,len(lst)):
#     temp=lst[i]
#     j=i-1
#     while j>=0 and temp < lst[j]:
#         lst=lst[:j+1]+lst[j]+lst[j+2:]
#         j-=1
#     lst=lst[:j+1]+temp+lst[j+2:]
# print(lst)

#program for list of characters 
lst=['c','b','a','B','A','C']
lst=lst
for i in range(1,len(lst)):
    temp=lst[i]
    t=temp.upper()
    j=i-1
    l=lst[j].upper()
    while j>=0 and t < l:
        lst[j+1]=lst[j]
        j-=1
        l=lst[j].upper()
    lst[j+1]=temp
print(lst)
