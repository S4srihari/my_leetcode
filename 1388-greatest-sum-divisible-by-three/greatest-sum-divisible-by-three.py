class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        tot = 0
        one = []
        two = []
        for num in nums:
            tot += num
            if num%3 == 1:
                one.append(num)
            elif num%3 == 2:
                two.append(num)
        if tot%3 == 0: return tot
        one.sort()
        two.sort()
        if tot%3 == 1:
            if len(two) < 2:
                return tot - one[0]
            elif len(one) < 1:
                return tot - two[0] - two[1] 
            return tot - min(one[0], two[0]+two[1])
        else:
            if len(one) < 2:
                return tot - two[0]
            elif len(two) < 1:
                return tot - one[0] - one[1]
            return tot - min(two[0], one[0]+one[1])
            