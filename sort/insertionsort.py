def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0  and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = temp

        

    return arr


arr1=[8,3,5,6,2,9,1]

print(insertionSort(arr1))