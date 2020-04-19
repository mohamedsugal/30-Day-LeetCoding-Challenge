from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Time complexity: O(mn)   Space complexity: O(mn)
        # n: rows   m: columns 
        if not grid: return 0 
        n, m = len(grid), len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                dp[i][j] += grid[i][j]
                if i > 0 and j > 0: 
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1])
                elif i > 0: 
                    dp[i][j] += dp[i-1][j]
                elif j > 0: 
                    dp[i][j] += dp[i][j-1]
        return dp[n-1][m-1]

grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]      

grid2 = [[1,2,5],
         [3,2,1]]  
solution = Solution()
print(solution.minPathSum(grid))
print(solution.minPathSum(grid2))