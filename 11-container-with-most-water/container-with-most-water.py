class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = 0
        l,r = 0, len(height)-1
        while l < r:
            volume = min(height[l],height[r]) * (r-l)
            max_volume = max(volume, max_volume)
            if height[l] <= height[r]:
                l += 1
            else :
                r -= 1
        return max_volume