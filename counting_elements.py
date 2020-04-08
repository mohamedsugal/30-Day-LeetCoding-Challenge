from typing import List

class Solution:
    @staticmethod
    def countElements(arr: List[int]) -> int:
        arr_set, count = set(), 0
        for i in arr: 
            arr_set.add(i)
        for x in arr:
            if x + 1 in arr_set: 
                count += 1
        return count

arrays = [[1,2,3], [1,1,3,3,5,5,7,7], [1,3,2,3,5,0], [1,1,2,2]]
answers = [2, 0, 3, 2]
solution = Solution()
i = 0
while i < len(arrays): 
    res = solution.countElements(arrays[i])
    if res == answers[i]: 
        print("Passed...")
    else: 
        print("Failed...")
    i += 1

