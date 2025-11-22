class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        s = SortedList()
        for i in range(len(nums)):
            if i >= indexDiff+1:
                s.remove(nums[i-indexDiff-1])
            if s and bisect_left(s, nums[i]-valueDiff) != bisect_right(s, nums[i]+valueDiff):
                return True
            s.add(nums[i])
        return False

