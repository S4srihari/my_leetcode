class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 1, max(candies)
        if k == 0 or k > sum(candies):
            return 0
        while left <= right:
            mid = left + (right-left)//2
            cnt = sum([i//mid for i in candies])
            if cnt < k:
                right = mid-1
            elif cnt >= k:
                left = mid +1
        return right