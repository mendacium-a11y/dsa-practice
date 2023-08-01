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

str1 = "aaaaabaaa"
a = palindrome(str1, 0, len(str1)-1)
print(a)