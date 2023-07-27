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

a = sayNum(435)
print()
# print(a)