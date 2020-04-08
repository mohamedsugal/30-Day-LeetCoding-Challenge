from typing import List 

class Solution:
    @staticmethod 
    def moveZeroes(nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0 
        for i in range(len(nums)): 
            if nums[i] != 0: 
                temp = nums[index]
                nums[index] = nums[i]
                nums[i] = temp 
                index += 1
        return nums 

nums = [0,1,0,3,12]
solution = Solution()
print(solution.moveZeroes(nums))
                
                