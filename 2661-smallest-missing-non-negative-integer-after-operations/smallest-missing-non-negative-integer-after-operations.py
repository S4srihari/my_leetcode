class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        store = [0]*value
        for i in nums:
            store[i%value] += 1

        min_freq = float('inf')
        min_idx = -1
        
        for i in range(value):
            if store[i] < min_freq:
                min_freq = store[i]
                min_idx = i
        
        return min_freq * value + min_idx