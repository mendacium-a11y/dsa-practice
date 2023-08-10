def subsets(nums):
    n = len(nums)
    result = []
    
    for i in range(2**n):
        subset = []
        print(i)
        print(subset)
        for j in range(n):
            print("inside 2nd fuction")
            if i & (1 << j):
                subset.append(nums[j])
            print(subset)
            print(j)
        result.append(subset)
    
    return result

a = [1, 2, 3]
print(subsets(a))
