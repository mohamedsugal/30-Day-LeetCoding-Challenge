from typing import List 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        left = 1 
        for i in range(len(nums)): 
            result += [left]
            left *= nums[i]
        right = 1 
        for i in range(len(nums)-1, -1, -1): 
            result[i] *= right 
            right *= nums[i]
        return result

nums = [1,2,3,4]
solution = Solution()
print(solution.productExceptSelf(nums))
    
        