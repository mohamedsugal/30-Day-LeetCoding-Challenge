from heapq import heappop, heappush, heapify
from typing import List 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)): 
            stones[i] *= -1
        heapify(stones)

        while len(stones) > 1: 
            stone1 = heappop(stones)
            stone2 = heappop(stones)
            if stone1 != stone2: 
                heappush(stones, stone1 - stone2)
        
        if not stones: 
            return 0 
        return -1 * heappop(stones)

stones = [2,7,4,1,8,1]
solution = Solution()
print(solution.lastStoneWeight(stones))