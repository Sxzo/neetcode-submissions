class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # def cc(i, curr_combo) = the number of distinct combos that add up to amount, starting from curr_combo

        memo = {}
        def cc(i, curr_sum):
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            
            if curr_sum == amount:
                return 1
            
            if curr_sum > amount:
                return 0
            
            total = 0
            for j in range(i, len(coins)):
                total += cc(j, curr_sum + coins[j])
            
            memo[(i, curr_sum)] = total
            return memo[(i, curr_sum)]

        
        return cc(0, 0)