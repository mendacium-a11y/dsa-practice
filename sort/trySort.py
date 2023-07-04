def selectionSort(arr):
    for i in range(len(arr)-1):
        min = i
        
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                min = j


        arr[min], arr[i] = arr[i], arr[min]

    return arr

def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]

    return arr


arr1=[6,3,5,9,1]

print(selectionSort(arr1))
print(bubbleSort(arr1))

