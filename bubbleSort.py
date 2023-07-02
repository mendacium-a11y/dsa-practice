def bubbleSort(arr):
    for i in range(0, len(arr)-1):

        for j in range(len(arr)-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j] 
        
    return (arr)


arr1 = [64, 45, 32, 96 , 22, 5, 43]

print(bubbleSort(arr1))
        