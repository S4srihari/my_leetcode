class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def Find(nums, low, high, element):
            while low <= high:
                mid = low + ((high - low) // 2)
                if nums[mid] >= element:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        nums.sort()
        pairs = 0
        for i in range(len(nums)):
            l = Find(nums, i + 1, len(nums) - 1, lower - nums[i])
            r = Find(nums, i + 1, len(nums) - 1, upper - nums[i]+1)
            pairs += r - l
        return pairs