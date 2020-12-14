# -*- coding: utf-8 -*-
"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""
# Solution 1
# binary search O(NLogN) time
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)-1):
            complement = target - numbers[i]
     
            low = i + 1
            high = len(numbers) - 1
            while low <= high:
                mid = (low + high) // 2

                if numbers[mid] == complement:
                    return [i+1, mid+1]

                elif numbers[mid] < complement:
                    low = mid + 1

                else:
                    high = mid - 1
                    
# Solution 2
# two pointers O(N) time
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            elif s < target:
                left += 1
            else:
                right -= 1