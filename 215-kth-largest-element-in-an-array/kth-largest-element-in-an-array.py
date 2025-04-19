class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for idx in range(k):
            h.append(nums[idx])
        heapq.heapify(h)
        for num in nums[k:]:
            heapq.heappush(h,num)
            heapq.heappop(h)
        return h[0]