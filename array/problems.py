#reverse an array

def reverseArr(arr):
    for i in range(int( len(arr) / 2 )):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i],arr[i]

    return arr


arr1 = [1,2,3,4,5,6,7,8,9]

print(reverseArr(arr1))