class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        prev = None
        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][1]: 
                val = stack.pop()
                res[val[0]] = i - val[0]
            stack.append([i, temp])
        
        return res 



