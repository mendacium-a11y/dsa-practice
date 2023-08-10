# reverse a string

def reverse (arr,i,j) :
    if (i>j):
        return arr
    
    arr[i], arr[j] = arr[j],arr[i]
    i += 1
    j -= 1
    return reverse(arr,i,j)

# str1 = "abdce"
# 
# a = reverse(list(str1),0,4)
# print("".join(a))

# palindrome checker
def palindrome(arr,i,j):
    if i > j:
        return True
    elif arr[i] != arr[j]:
        return False
    else:

        i += 1
        j -= 1
        return palindrome(arr, i, j)

# str1 = "aaaaabaaa"
# a = palindrome(str1, 0, len(str1)-1)
# print(a)

# calculate power of a num
def power( a , b ):
    if b == 0:
        return 1
    elif b == 1:
        return a
    
    ans = power(a, b//2)
    if b%2 == 0:
        return ans*ans
    else:
        return a*ans*ans
# print(power(3,10))


# bubble sort using recursion
def bubble(arr,len):
    if len == 1:
        return arr
    for i in range(len-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    len -= 1
    return bubble(arr, len)

arr1 = [1,4,3,9,2,8,2,3]
a = bubble(arr1, len(arr1))
print(a)