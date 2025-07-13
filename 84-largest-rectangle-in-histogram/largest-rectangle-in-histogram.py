class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        """for left in range(len(heights)):
            min_seen = heights[left]
            for right in range(left,len(heights)):
                if heights[right] < min_seen:
                    min_seen = heights[right]
                area = (right - left + 1)*min_seen
                if area > max_area:
                    max_area = area"""
        n = len(heights)
        stack = []
        for idx in range(n):
            start = idx
            while stack and stack[-1][0] > heights[idx]:
                height, left = stack.pop()
                area = (idx - left)*height 
                max_area = max(area, max_area)
                start = left
            stack.append((heights[idx], start))
                
            
        while stack:
            height, left = stack.pop()
            area = (n - left)*height 
            max_area = max(area, max_area)

        return max_area