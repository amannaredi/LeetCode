class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        
        profit = 0
        for r in range(1,len(prices)):
            max_profit = 0
            if prices[l]>prices[r]:
                l = r
            max_profit = max(max_profit,prices[r]-prices[l])
            l = r
            profit+=max_profit
        return profit