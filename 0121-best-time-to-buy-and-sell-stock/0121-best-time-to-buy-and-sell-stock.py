class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit
        # n = len(prices)
        # l = 0
        # max_profit = 0
        # for r in range(1,n):
        #     if prices[l] > prices[r]:
        #         l +=1
        #     else:
        #         # prices[l] < prices[r]:
        #         diff = prices[r] - prices[l]
        #         max_profit = max(diff, max_profit)

        # return max_profit

             # if n == 2:
        #     if prices[1] - prices[0] >0:
        #         return prices[1] - prices[0]
        #     else:
        #         return 0