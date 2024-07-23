class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        max_profit = 0
        for r in range(1,n):
            if prices[l] > prices[r]:
                print("line8",(l,r))
                l = r
            else:
                print("line10",(l,r))
                diff = prices[r] - prices[l]
                max_profit = max(max_profit, diff)

        return max_profit

             # if n == 2:
        #     if prices[1] - prices[0] >0:
        #         return prices[1] - prices[0]
        #     else:
        #         return 0