from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count, max_length = 0, 0
        table = {0: 0}
        for idx, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in table:
                max_length = max(max_length, idx - table[count])
            else:
                table[count] = idx
        return max_length


nums = [0, 0, 1, 0, 0, 0, 1, 1]
Solution = Solution()
print(Solution.findMaxLength(nums))
