"""
Two Pointers - Container With Most Water
Given an array of heights where each element represents the height of a vertical line, find two lines that together with the x-axis form a container that holds the most water. Return the maximum area of water the container can hold.
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49 (between heights 8 and 7 at indices 1 and 8)

This builds nicely on your two-pointer experience from problems like "Valid Palindrome" and "Two Sum"!
"""

def container_with_max_water(nums):
    n = len(nums)
    left = 0
    right = n-1
    max_water = 0

    while left < right:
        min_value = min(nums[left], nums[right])
        max_water = max(max_water, min_value*(right - left))
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

if __name__=="__main__":
    print (container_with_max_water([1,8,6,2,5,4,8,3,7]))