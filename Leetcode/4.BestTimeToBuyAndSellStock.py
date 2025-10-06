"""
Here's the Best Time to Buy and Sell Stock problem from LeetCode:

Problem Statement
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Examples

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Example 3:

Input: prices = [9,2,5,9,1,4,5,6]


Constraints
1 <= prices.length <= 10⁵
0 <= prices[i] <= 10⁴
Key Points
You must buy before you sell (can't sell on an earlier day)
You can only make one transaction (one buy + one sell)
If no profit is possible, return 0


This is a classic problem that can be solved in O(n) time with one pass! Want to give it a try?
"""


def max_profit(prices):
    max_returns = 0
    min_value = float("inf")
    for i, price in enumerate(prices):
        if price < min_value:
            min_value = price
        if price - min_value > max_returns:
            max_returns = price - min_value
    return max_returns

if __name__=="__main__":
    max_returns = max_profit([9,2,5,9,1,4,5,6])
    print(max_returns)

