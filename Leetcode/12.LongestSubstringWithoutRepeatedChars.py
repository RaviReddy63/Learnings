"""
Problem Statement
Given a string s, find the length of the longest substring without repeating characters.
A substring is a contiguous sequence of characters within a string.
Examples
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:
Input: s = ""
Output: 0
Example 5:
Input: s = "abcdefg"
Output: 7
Constraints

0 <= s.length <= 5 * 10⁴
s consists of English letters, digits, symbols and spaces.

"""

def longest_substring(s):
    left = 0
    max_length = 0
    chars = set()

    for i in range(len(s)):
        while s[i] in chars:
            chars.remove(s[left])
            left = left + 1

        chars.add(s[i])

        max_length = max(max_length, i - left +1)

    return max_length

if __name__=="__main__":
    print (longest_substring("bbbbb"))