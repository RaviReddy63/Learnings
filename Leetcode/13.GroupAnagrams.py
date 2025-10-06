"""
Problem Statement
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Examples
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
- "eat", "tea", "ate" are anagrams
- "tan", "nat" are anagrams
- "bat" stands alone
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]
Constraints

1 <= strs.length <= 10⁴
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""
def groupAnagrams(strs):
    anagrams = {}
    
    for word in strs:
        # Sort the word to create a key
        sorted_word = ''.join(sorted(word))
        
        # Add to the group
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)
    
    return list(anagrams.values())

def groupAnagrams(strs):
    anagrams = {}
    
    for word in strs:
        # Count characters (a-z)
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        
        # Use tuple of counts as key
        key = tuple(count)
        
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    
    return list(anagrams.values())
