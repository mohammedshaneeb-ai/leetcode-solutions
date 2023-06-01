"""Q: 121. Best Time to Buy and Sell Stock:
 You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        min_price = prices[0] 
        max_profit = 0 

        for price in prices[1:]:
            min_price = min(min_price, price)

            potential_profit = price - min_price

            max_profit = max(max_profit, potential_profit)

        return max_profit

# Object creation
obj = Solution()

# Example 1
prices = [7,1,5,3,6,4]
# Expected output : 5
print(obj.maxProfit(prices))

# Example 2
prices = prices = [7,6,4,3,1]
# Expected output : 0
print(obj.maxProfit(prices))