#reverse an array after a particular index

def reverseArr(arr,n):
    start = n+1
    end = len(arr)-1
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]

        start +=1
        end -= 1

    return arr


arr1= [1,2,3,4,5,6]

print(reverseArr(arr1,1))

