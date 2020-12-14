# -*- coding: utf-8 -*-
"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        min_diff = float('inf')
        result = 0
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            # two pointer
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if l - 1 != i and nums[l] == nums[l-1]:
                    l += 1
                    continue
                
                if r + 1 <= len(nums) -1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return target
                elif s > target:
                    r -= 1
                    curr_diff = abs(s - target)
                    if curr_diff < min_diff:
                        result = s
                        min_diff = curr_diff
                else:
                    l += 1
                    curr_diff = abs(s - target)
                    if curr_diff < min_diff:
                        result = s
                        min_diff = curr_diff
        
        return result

