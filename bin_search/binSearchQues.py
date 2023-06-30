def first(arr, key):
    start = 0
    end = len(arr)
    
    mid = start+(end-start)//2
    ans_start = -1
    ans_end = -1

    while(start<=end):
        if arr[mid] == key:
            ans = mid
            end = mid-1

        elif arr[mid] > key:
            end = mid-1

        elif arr[mid] < key:
            start = mid+1

        mid = start+(end-start)//2

    return ans

def last(arr, key):

    start = 0

    end = len(arr)

    

    mid = start+(end-start)//2

    ans_start = -1

    ans_end = -1



    while(start<end):

        if arr[mid] == key:

            ans = mid

            start = mid+1



        elif arr[mid] > key:

            end = mid-1



        elif arr[mid] < key:

            start = mid+1



        mid = start+(end-start)//2



    return ans

arr1 = [1,2,2,5,5,5,6,8,9]
print(first(arr1,5))
print(last(arr1,5))
