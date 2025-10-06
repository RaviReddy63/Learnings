"""
Problem Statement
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Examples
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 step to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]

Explanation: 
rotate 1 step to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Example 3:
Input: nums = [1,2,3,4,5], k = 7
Output: [4,5,1,2,3]

Explanation: k = 7 is the same as k = 2 (since 7 % 5 = 2)
Constraints

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5

Key Points to Consider

You must modify the array in-place with O(1) extra space
k might be larger than the array length (use modulo)
Try to solve it in O(n) time complexity

"""

def rotate_array(nums, k):

    n = len(nums)


    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right -= 1

    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)
    return nums

if __name__=="__main__":
    print (rotate_array(nums = [1,2,3,4,5,6,7], k = 3))