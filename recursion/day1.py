#factorial
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

# a = factorial(6)
# print(a)

# fibbionacci series

def fibbionacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibbionacci(n-1) + fibbionacci(n-2)


# a = fibbionacci(6)
# print(a)

num = ['zero','one','two','three','four','five','six','seven','eight','nine']

def sayNum(n):
    if n == 0:
        return 
    
    sayDigit = n%10
    n = int(n/10)

    sayNum(n)
    print(num[sayDigit], end=" ")

# a = sayNum(435)
# print()/
# print(a)

def isSorted(arr, n):
    
    n -= 1

    if n <= 0:
        return True
    elif arr[n-1] > arr[n]:
        return False
    else:
        output = isSorted(arr,n-1)
        return output

# a = [2,3,5,7,6,8]
# ist = isSorted(a,6)
# print(ist)

#sum using recursion
def sum(arr,n):
    
    if n == 1:
        return arr[n-1]
    return arr[n-1] + sum(arr,n-1)


# a = [1,2,3,4,6,4]
# `print(sum(a,6))

#linear search recursion
def linSearch(arr, n, len):
    if len == 0:
        return -1
    elif arr[len-1] == n:
        return len-1
    else:
        return linSearch(arr, n, len-1)

a = [1,2,3,4,5]
print(linSearch(a,9,5))


# start and end index using bin search
def checker (arr,k):
    n = len(arr)
    start = 0
    end = n-1
    mid = start + (end - start)//2

    