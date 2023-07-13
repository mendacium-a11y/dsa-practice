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

# print(reverseArr(arr1,1))


#move zeroes to the end in an array

def moveZero(arr):
    i = 0

    for j in range(i,len(arr)):
        if arr[j] != 0:
            arr[i],arr[j] = arr[j], arr[i]
            i+=1

    return (arr)


arr2 = [0,2,0,4,5,0,6,7]

# print(moveZero(arr2))

# rotate array

def rotate(arr, k):
    newArr = [0]*len(arr)
    for i in range(len(arr)):
        newArr[(i+k)%len(arr)] = arr[i]

    return newArr

arr3 = [1,2,3,4,5,6,6,7]

# print(rotate(arr3, 3))


#check if a string is a palindrome

def palindromeChecker(arr):
    n = len(arr)
    newArr = arr.split()
    newArr = "".join(newArr)
    
    i = 0
    while( i < n):
        if(arr[i] != arr[n-i-1]):
            return -1
        i += 1
    
    return True


string1 = "dad"

print(palindromeChecker(string1))