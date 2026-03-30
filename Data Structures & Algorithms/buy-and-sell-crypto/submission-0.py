class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        
        for r in range(1, len(prices)):
            # found cheaper buying price
            if prices[r] < prices[buy]:
                buy = r
            
            # update current profit
            max_profit = max(max_profit, prices[r] - prices[buy])

        return max_profit
