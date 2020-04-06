from typing import List 

class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        max_profit = 0 
        for i in range(len(prices)-1): 
            if prices[i] < prices[i+1]: 
                max_profit += prices[i+1]-prices[i]
        return max_profit

prices = [[7,1,5,3,6,4], [1,2,3,4,5], [7,6,4,3,1]]
answers = [7, 4, 0]
solution = Solution()
i = 0 
while i < len(prices): 
    res = solution.maxProfit(prices[i])
    if answers[i] == res: 
        print("Passed...")
    else: 
        print("Failed...")
    i += 1
