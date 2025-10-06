"""
Problem Statement
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Examples
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Example 3:
Input: n = 4
Output: 5
Explanation: There are five ways:
1. 1+1+1+1
2. 1+1+2
3. 1+2+1
4. 2+1+1
5. 2+2


Constraints

1 <= n <= 45


"""

def climbing_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    prev1 = 2
    prev2 = 1


    for i in range(3, n+1):
        total_steps = prev1 + prev2
        prev2 = prev1
        prev1 = total_steps

    return total_steps

if __name__=="__main__":
    print(climbing_stairs(10))
