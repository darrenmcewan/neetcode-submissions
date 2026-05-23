class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = 0
        for i in range(0,len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            else:
                maxProfit = max(maxProfit, prices[i] - prices[buy])

        return maxProfit