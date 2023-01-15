class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        for i in prices[1:]:
            if buy>i: buy = i
            if i-buy>sell: sell = i-buy
        return sell
        
