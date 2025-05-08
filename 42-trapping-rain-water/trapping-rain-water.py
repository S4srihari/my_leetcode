class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = height[0]
        water = 0
        for i in range(1,n-1):
            right = max(height[i+1:])
            if min(left,right) - height[i] > 0 :
                water += min(left,right) - height[i]
            if left < height[i]:
                left = height[i]
        return water