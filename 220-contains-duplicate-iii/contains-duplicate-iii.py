class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        for i, n in enumerate(nums):
            bucket_idx = n // valueDiff if valueDiff != 0 else n
            if bucket_idx in buckets:
                return True
            if (bucket_idx - 1) in buckets and n - buckets[bucket_idx - 1] <= valueDiff:
                return True
            if (bucket_idx + 1) in buckets and buckets[bucket_idx + 1] - n <= valueDiff:
                return True
            buckets[bucket_idx] = n
            if i >= indexDiff:
                expired =  nums[i-indexDiff] // valueDiff if valueDiff != 0 else nums[i-indexDiff]
                del buckets[expired]
        return False