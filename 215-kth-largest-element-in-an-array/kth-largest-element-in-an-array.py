class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s = SortedList()
        for num in nums:
            if len(s) < k:
                s.add(num)
            else :
                if s[0] < num :
                    s.pop(0)
                    s.add(num)
        return s[0]