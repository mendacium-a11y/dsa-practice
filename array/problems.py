#reverse an array

def reverseArr(arr):
    for i in range(int( len(arr) / 2 )):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i],arr[i]

    return arr


arr1 = [1,2,3,4,5,6,7,8,9]

# print(reverseArr(arr1))

#find max and min in array

def maxMin(arr):
    min = arr[0]
    max = arr[0]
    
    for i in range(1,len(arr)):
        if (arr[i] > max):
            max = arr[i]
        elif (arr[i] < min):
            max = arr[i]

    return f"min:{min} max:{max}"  



arr2 = [2,5,3,7,13,44,64,5,99,47,36]
print(maxMin(arr2))