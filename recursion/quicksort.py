def partition (arr, start, end) :
    pivot = arr[0]

    count = 0
    for i in range(1,len(arr)):
        if arr[i] <= pivot:
            count +=1

    pivotIndex = start+count

    arr[start],arr[pivotIndex] = arr[pivotIndex], arr[start]

    i = start
    j = end
    while(i < pivotIndex and j > pivotIndex):
        
        while(arr[i] < pivot):
            i+=1
        
        while(arr[j] > pivot):
            j-=1
            
        if (i < pivotIndex and j > pivotIndex):
            arr[i],arr[j] = arr[j],arr[i]

    return pivotIndex

def quicksort(arr, start, end):
    if start >= end:
        return 
    
    p  = partition(arr, start, end)

    quicksort(arr,start, p-1)
    quicksort(arr,p+1,end)

unsorted_list = [50, 10, 90, 30, 70, 40, 80, 60, 20]
sorted_list = quicksort(unsorted_list,0,len(unsorted_list)-1)
print(sorted_list)
     