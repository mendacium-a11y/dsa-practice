def pivot(arr):
    start = 0
    end = len(arr)
    mid = int(start + (end-start)/2)

    while(start<end):

        if (arr[mid] >= arr[start]):
            start = mid+1
        elif (arr[mid] <= arr[start] ):
            end = mid
        mid = int(start + (end-start)/2)

    return arr[start]

arr1=[4,5,6,1,2,3]

print(pivot(arr1))