# reverse a string

def reverse (arr,i,j) :
    if (i>j):
        return arr
    
    arr[i], arr[j] = arr[j],arr[i]
    i += 1
    j -= 1
    return reverse(arr,i,j)

str1 = "abdce"

a = reverse(list(str1),0,4)
print("".join(a))