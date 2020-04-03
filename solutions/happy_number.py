class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Input: 19
        Output: true
        Explanation: 
        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 02 = 1
        '''
        seen = [] # array to keep the numbers already seen 
        while n != 1: 
            temp = 0
            if n in seen: 
                return False
            seen.append(n)
            for i in str(n): 
                temp += int(i)**2
            n = temp
        return True
    
n = 19
solution = Solution()
print(solution.isHappy(n))
        