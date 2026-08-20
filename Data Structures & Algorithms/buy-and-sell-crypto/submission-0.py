class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1,n):
                if prices[i] < prices[j]:
                    if maxprofit < prices[j] - prices[i]:
                        maxprofit = prices[j] - prices[i]

        return maxprofit
                