class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1,2,3,4], h = 9 
        # k = 1
        # k = max(piles)

        def get_hours_to_eat(rate):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
            
            return hours

        left = 1
        right = max(piles)

        min_rate = max(piles)
        while left <= right:
            mid = (left + right) // 2

            hours_to_eat = get_hours_to_eat(mid)

            if hours_to_eat > h:
                left = mid + 1
            else:
                min_rate = min(min_rate, mid)
                right = mid - 1
        
        return min_rate



        