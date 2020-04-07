from typing import List 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}
        for word in strs: 
            key = self.checkAnagram(word)
            if key in groupings: 
                groupings[key].append(word)
            else: 
                groupings[key] = [word]
        return [*groupings.values()]
            
    @staticmethod
    def checkAnagram(word: str) -> tuple: 
        alpha = [0] * 26 
        for letter in word: 
            alpha[ord(letter) - ord('a')] += 1
        return tuple(alpha)

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
print(solution.groupAnagrams(strs))


