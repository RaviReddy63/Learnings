"""
Problem Statement
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Examples
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints

1 <= s.length, t.length <= 5 * 10⁴
s and t consist of lowercase English letters

"""

def valid_anagram(s,t):
    counts = {}

    for i in s:
        counts[i] = counts.get(i, 0) + 1

    for i in t:
        counts[i] = counts.get(i,0) - 1
        if counts[i] < 0:
            return False
    return True

if __name__=="__main__":
    print(valid_anagram(s = "rat", t = "tar"))