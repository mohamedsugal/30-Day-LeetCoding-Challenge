from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s = list(s)
        for direction, amount in shift: 
            if direction == 0: 
                self.rotate_left(s, amount)
            else: 
                self.rotate_right(s, amount)
        return "".join(s)

    def rotate_left(self, s, k): 
        k %= len(s)
        self.reverse(s, k, len(s) - 1)
        self.reverse(s, 0, k - 1)
        self.reverse(s, 0, len(s) - 1)
        return s
    
    def rotate_right(self, s, k): 
        k %= len(s)
        self.reverse(s, 0, len(s) - 1)
        self.reverse(s, 0, k - 1)
        self.reverse(s, k, len(s) - 1)
        return s

    def reverse(self, s, start, end): 
        while start < end: 
            temp = s[start]
            s[start] = s[end]
            s[end] = temp 
            start += 1
            end -= 1


s = "abcdefg"
shift = [[1,1],[1,1],[0,2],[1,3]]
solution = Solution()
print(solution.stringShift(s, shift))


