class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Initialize our minimum price as the first in the list
        min_price = prices[0]
        # Initialize profit as the 0
        max_profit = 0

        # iterate over the list of prices once
        for price in prices:
            # min_price will be the minimum of the current price and our initialized price
            min_price = min(price,min_price)
            # max_profit will take the current price - min price and compare with our current max_profit
            max_profit = max(price - min_price, max_profit)
        
        return max_profit
    