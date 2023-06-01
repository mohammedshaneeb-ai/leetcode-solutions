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

obj = Solution()

# Example 1
prices = [7,1,5,3,6,4]
# Expected output : 5
print(obj.maxProfit(prices))

# Example 2
prices = prices = [7,6,4,3,1]
# Expected output : 0
print(obj.maxProfit(prices))

