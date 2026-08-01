class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = float('inf')
        r = 0
        maxProfit = 0
        for p in prices:
            if p < l:
                l = p
                r = 0
                continue
            
            if p > r:
                r = p
                maxProfit = max(r - l, maxProfit)

        return maxProfit

        