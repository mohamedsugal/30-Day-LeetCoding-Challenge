class Solution:
    def checkValidString(self, s: str) -> bool:
        # Time complexity: O(n)
        # Space complexity: O(n) use of the stack 
        parenthesis, asterisk = [], []
        for i, c in enumerate(s): 
            if c == '(': parenthesis.append(i)
            elif c == '*': asterisk.append(i)
            else: 
                if parenthesis: parenthesis.pop()
                elif asterisk: asterisk.pop()
                else: return False 

        while parenthesis: 
            if asterisk == []: return False
            if parenthesis[-1] < asterisk[-1]: 
                parenthesis.pop()
                asterisk.pop()
            else: return False 
        return True 
            
           

s = "(**)"
solution = Solution()
print(solution.checkValidString(s))