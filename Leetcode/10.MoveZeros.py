"""
Problem Statement
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note: You must do this in-place without making a copy of the array.
Examples
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]
Example 3:
Input: nums = [1,2,3,0,0,4,0,5]
Output: [1,2,3,4,5,0,0,0]
Constraints

1 <= nums.length <= 10⁴
-2³¹ <= nums[i] <= 2³¹ - 1

Follow-up
Could you minimize the total number of operations done?
"""

def move_zeros(nums):
    first_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[first_zero], nums[i] = nums[i], nums[first_zero]
            first_zero = first_zero + 1
    return nums

if __name__=="__main__":
    print (move_zeros([0,1,0,3,12]))
            