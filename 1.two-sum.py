#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}

        for i, num in enumerate(nums):
            if target - num in numToIndex:
             return numToIndex[target - num], i
            numToIndex[num] = i
        
# @lc code=end

