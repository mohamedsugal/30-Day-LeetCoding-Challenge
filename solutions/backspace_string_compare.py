class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.compare(S) == self.compare(T)
    
    @staticmethod
    def compare(str): 
        stack = []
        for char in str: 
            if char == "#": 
                if stack: 
                    stack.pop()
            else: 
                stack.append(char)
        return "".join(stack)

        
        



S = "a#c"
T = "b"

solution = Solution()
print(solution.backspaceCompare(S, T))
