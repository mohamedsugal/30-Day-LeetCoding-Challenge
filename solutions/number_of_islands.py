from typing import List 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands_count = 0
        for row in range(len(grid)): 
            for col in range(len(grid[0])): 
                if grid[row][col] == '1': 
                    islands_count += 1
                    self.DFS(grid, row, col)
        return islands_count
    
    def DFS(self, grid, row, col): 
        # base cases: 
        # 1) if row < 0 or row >= len(grid)
        # 2) if col < 0 or col >= len(grid[0])
        # 3) if row, col == '0'
        if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])) or (grid[row][col] == '0'): 
            return 
        grid[row][col] = '0'
        self.DFS(grid, row - 1, col)
        self.DFS(grid, row + 1, col)
        self.DFS(grid, row, col - 1)
        self.DFS(grid, row, col + 1)

grid1 = [['1','1','1','1','0'], 
         ['1','1','0','1','0'], 
         ['1','1','0','0','0'], 
         ['0','0','0','0','0']]
        
grid2 = [['1','1','0','0','0'],
         ['1','1','0','0','0'],
         ['0','0','1','0','0'],
         ['0','0','0','1','1']]

solution = Solution()
print(solution.numIslands(grid1))
print(solution.numIslands(grid2))




