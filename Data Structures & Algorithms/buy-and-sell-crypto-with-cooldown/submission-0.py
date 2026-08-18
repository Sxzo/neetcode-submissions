class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # def mp(i, profit) = maxProfit achievable from prices[i::], with coin_flag representing ownership
        # If you dont own a coin, your options are to buy one or not buy one

        memo = {}
        def mp(i, coin_flag):
            
            if (i, coin_flag) in memo:
                return memo[(i, coin_flag)]
            
            if i >= len(prices):
                return 0
            
            if not coin_flag:
                memo[(i, coin_flag)] = max(-1 * prices[i] + mp(i + 1, True), mp(i + 1, False))
            else:
                memo[(i, coin_flag)] = max(prices[i] + mp(i + 2, False), mp(i + 1, True))
            
            return memo[(i, coin_flag)]

        
        return mp(0, False)
            
            
        