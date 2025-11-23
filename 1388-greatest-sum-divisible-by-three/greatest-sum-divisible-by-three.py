class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        tot = 0
        o1, o2, t1, t2  = 100000, 100000, 100000, 100000
        for num in nums:
            tot += num
            if num%3 == 1:
                if num <= o1:
                    o2 = o1
                    o1 = num
                elif num < o2:
                    o2 = num
            elif num%3 == 2:
                if num <= t1:
                    t2 = t1
                    t1 = num
                elif num < t2:
                    t2 = num
        if tot%3 == 0: return tot
        elif tot%3 == 1:
            return tot - min(o1, t1 + t2)
        else:
            return tot - min(t1, o1+o2)
            