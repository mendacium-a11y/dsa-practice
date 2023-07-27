def linSearch(arr, n):
    for i in range(len(arr)):
        if arr[i] == n :
            return i
    else:
        return -1

bin = [2,3,4,5,6,14,20]

print(linSearch(bin,14))