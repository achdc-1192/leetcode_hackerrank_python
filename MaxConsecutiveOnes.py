'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prevmax = 0
        currmax = 0
        i = 0
        while i <= len(nums)-1:
            if nums[i] == 1:
                currmax += 1
                i += 1
            else:
                if currmax > prevmax:
                    prevmax = currmax
                    currmax = 0
                else:
                    currmax = 0
                i += 1
        return max(currmax,prevmax)
      
