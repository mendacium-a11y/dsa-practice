def BinSearch2d(arr, n):
    row = len(arr)
    col = len(arr[0])
    total = row*col 
    start = 0
    end = (row*col) -1
    mid = int(start + (end - start)/2)

    while (start <= end):
        element = arr[int(mid/col)][int(mid/row)]

        if(element == n):
            return mid
        
        elif(element > n):
            end = mid-1
        else:
            start = mid+1 
        
        mid = int(start + (end - start)/2)


arr1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(BinSearch2d(arr1,12))