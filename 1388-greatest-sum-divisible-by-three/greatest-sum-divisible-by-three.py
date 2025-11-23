class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        tot = 0
        o1, o2, t1, t2  = None, None, None, None
        for num in nums:
            tot += num
            if num%3 == 1:
                if o1 == None:
                    o1 = num
                elif num <= o1:
                    o2 = o1
                    o1 = num
                elif o2 == None:
                    o2 = num
                elif num < o2:
                    o2 = num
            elif num%3 == 2:
                if t1 == None:
                    t1 = num
                elif num <= t1:
                    t2 = t1
                    t1 = num
                elif t2 == None:
                    t2 = num
                elif num < t2:
                    t2 = num
        print(o1, o2, t1, t2)
        if tot%3 == 0: return tot
        elif tot%3 == 1:
            if t2 is None:
                return tot - o1
            elif o1 is None:
                return tot - t1 - t2 
            return tot - min(o1, t1 + t2)
        else:
            if o2 is None:
                return tot - t1
            elif t1 is None:
                return tot - o1 - o2
            return tot - min(t1, o1+o2)
            