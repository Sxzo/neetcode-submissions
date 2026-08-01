class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_positions = []
        for i,p in enumerate(position): 
            sorted_positions.append((position[i], speed[i]))
        sorted_positions.sort()
        # print(sorted_positions)
        # [3,4,5,6,7,8] [4...] = [3, 2, 2, 1, 1, 1]
        # [0,1,4,7] [1,2,2,1] = [10, 5, 3, 3]
        prev_time = float('-inf')
        total_fleets = 0
        while sorted_positions:
            position_, speed_ = sorted_positions.pop()
            time = (target - position_) / speed_
            # print(time)
            while sorted_positions and time >= (target - sorted_positions[-1][0]) / sorted_positions[-1][1]:
                sorted_positions.pop()
            total_fleets += 1
        
        return total_fleets