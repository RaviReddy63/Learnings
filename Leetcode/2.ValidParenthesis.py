"""
Problem Statement
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Examples
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true


Constraints

1 <= s.length <= 10⁴
s consists of parentheses only '()[]{}'

"""

def valid_parentheses(s):
    expected = []
    closing = {
        '{': '}',
        '[': ']',
        '(': ')'
    }

    for i in s:
        if i in closing:
            expected.append(closing[i])
        elif expected and i == expected[-1]:
            expected.pop(-1)
        else:
            return False
    
    if len(expected) > 0:
        return False
    return True
    
if __name__=="__main__":
    valid = valid_parentheses('([]')
    print (valid)
