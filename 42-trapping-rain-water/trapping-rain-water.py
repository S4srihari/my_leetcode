class Solution:
    def trap(self, height: List[int]) -> int:
        """n = len(height)
        left = height[0]
        water = 0
        for i in range(1,n-1):
            right = max(height[i+1:])
            if min(left,right) - height[i] > 0 :
                water += min(left,right) - height[i]
            if left < height[i]:
                left = height[i]
        return water"""

        n = len(height)
        left = 0
        right = n-1
        max_left = height[0]
        max_right = height[n-1]
        water = 0
        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                water += max_left - height[left]
            else :
                right -= 1
                max_right = max(max_right, height[right])
                water += max_right - height[right]
        return water