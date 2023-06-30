def binSearch(arr, num):
    start = 0
    end = len(arr)-1

    center = (start+end)//2
    
    while(end>=start):
        if arr[center] == num:
            return center
        elif arr[center] > num:
            end = center - 1
        elif arr[center] < num:
            start = center + 1

        center = (start+end)//2
        




bin = [2,3,4,5,6,14,20]

print(binSearch(bin, 14))
