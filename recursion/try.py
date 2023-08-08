
# def maximumCount(nums):
        
        
#         if nums[-1] == 0 or nums[0] == 0 or nums[0] > 0 or nums[-1] < 0:
#             return len(nums)

#         start = 0
#         end = len(nums)-1
#         mid = start + (end-start)//2
        
#         pos=0
#         # calculating the first +ve num
#         while ( start <= end ):
#             if nums[mid] > 0:
#                 end = mid-1
#                 pos = mid
#             elif nums[mid] < 0:
#                 start = mid+1
#             mid = start + (end-start)//2

        
        

        # return max(len(nums)-pos,pos+1)


def maximumCount(self, nums: List[int]) -> int:
        if nums[0] == 0 and nums[-1] ==0:
            return 0
        if nums[0] > 0 or nums[-1] < 0:
            return len(nums)

        pos_count, neg_count = 0, 0

        for num in nums:
            if num > 0:
                pos_count += 1
            elif num < 0:
                neg_count += 1

        return max(pos_count, neg_count)
                
nums = [-2,-1,-1,1,2,3,6,9,10]
print(maximumCount(nums))