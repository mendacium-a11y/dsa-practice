def selSrt(arr):

    for i in range (len(arr)-1):
        minIndex = i

        for j in range(i+1,len(arr)-1):
            if arr[minIndex] > arr[j]:
                minIndex = j

        arr[minIndex],arr[i] = arr[i], arr[minIndex]    

    return arr



arr1 = [22,45,7,34,77]

print(selSrt(arr1))