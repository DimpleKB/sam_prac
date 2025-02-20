''' worst and average time complexity is o(n^2)
    and average case time complexity is o(n)
    '''

def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]

def optimized_bubble_sort(array):
    for i in range(len(array)-1):
        sorted=True
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                sorted=False
        if sorted:
            return
array=[5,4,3,2,1]
optimized_bubble_sort(array)
print(array)