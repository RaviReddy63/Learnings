"""
Problem Statement
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Examples
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
Constraints

1 <= s.length <= 2 * 10⁵
s consists only of printable ASCII characters.

"""

import re

def valid_palindrome(s):
    s = re.sub(r'[^a-zA-Z]', '',s)
    s = s.lower()
    # snew = s
    snew = list(s)
    for i in range(0, len(s)//2):
        snew[i], snew[len(s) - i - 1] = snew[len(s) - i - 1], snew[i]
    snew = "".join(snew)
    if snew == s:
        return True
    else:
        return False

if __name__=="__main__":
    print (valid_palindrome("race a car"))