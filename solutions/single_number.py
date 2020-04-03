class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        Input: [4,1,2,1,2]
        Output: 4
        '''
        ans = 0
        for i in nums: 
            ans = ans ^ i 
        return ans

nums = [4,1,2,1,2]
solution = Solution()
print(solution.singleNumber(nums))
    
            