"""
Problem Statement
Given an integer array nums, find the subarray with the largest sum, and return its sum.
A subarray is a contiguous non-empty sequence of elements within an array.
Examples

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
Constraints

1 <= nums.length <= 10⁵
-10⁴ <= nums[i] <= 10⁴
"""

def max_sub_array(nums):
    sum = nums[0]
    max_sum = nums[0]
    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        if sum+nums[i] < nums[i]:
            sum = nums[i]
            temp_start = i
        else:
            sum = sum + nums[i]
        
        if max_sum < sum:
            max_sum = sum
            start = temp_start
            end = i

    return max_sum, nums[start: end+1]

if __name__=="__main__":
    print (max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))