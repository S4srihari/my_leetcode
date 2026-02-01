class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        heap = []
        for i in range(1,len(nums)):
            heapq.heappush(heap, -nums[i])
            if i >= 3:
                heapq.heappop(heap)
        tot = nums[0]
        while heap:
            tot += heapq.heappop(heap)*(-1)
        return tot