
def msort(arr):
    
    if len(arr) <= 1:
        return arr
    
    
    mid = len(arr)//2
    
    
    left = msort(arr[:mid])
    right = msort(arr[mid:])

    return merge(left, right)

def merge(left,right):
    sorted_arr = []
    i = 0
    j = 0
    

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr += left[i:]
    sorted_arr += right[j:]
        
    return sorted_arr


a = [45,34,77,12,97,99,54,63,143,125]
print(msort(a))