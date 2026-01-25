class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0
        left_boundary = [-1]*n
        right_boundary = [n]*n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
    
            if stack:
                left_boundary[i] = stack[-1]

            stack.append(i)
        
        stack.clear()
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                right_boundary[i] = stack[-1]
            stack.append(i)

        max_area = 0
        for i in range(n):
            area = heights[i] * (right_boundary[i]-left_boundary[i] - 1)
            max_area = max(area, max_area)
        return max_area