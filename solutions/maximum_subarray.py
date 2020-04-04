from typing import List 

class Solution:
    @staticmethod
    def max_subarray(nums: List[int]) -> int:
        result = curr_sum = float('-inf')
        for i in nums: 
            curr_sum = max(i, curr_sum+i)
            result = max(result, curr_sum)
        return result 
                    
nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
print(solution.max_subarray(nums))
