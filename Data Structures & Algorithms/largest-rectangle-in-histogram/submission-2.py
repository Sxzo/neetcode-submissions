class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack: (i, height)
        stack = []
        largest_area = 0
        for i, height in enumerate(heights):
            start = i 
            while stack and height < stack[-1][1]:
                val = stack.pop()
                largest_area = max((i - val[0]) * val[1], largest_area)
                start = val[0]
            stack.append([start, height])
        
        for i, height in stack:
            largest_area = max(height * (len(heights) - i), largest_area)
        
        return largest_area