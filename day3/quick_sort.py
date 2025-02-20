def quick_sort(numbers,low,high):
    if low < high:
        j = low
        pivot = numbers[high]
        for i in range(low,high):
            if numbers[i] < pivot:
                numbers[i], numbers[j] = numbers[j], numbers[i] # move the smaller element to the left
                j += 1
        numbers[j], numbers[high] = numbers[high], numbers[j] # place the pivot element in its final position
        quick_sort(numbers,low,j-1)
        quick_sort(numbers,j+1,high)

print('Enter the input numbers')
numbers = list(map(int, input().split()))

print(f'Input Array is: {numbers}')
quick_sort(numbers,0,len(numbers)-1)
print(f'sorted Array is: {numbers}')