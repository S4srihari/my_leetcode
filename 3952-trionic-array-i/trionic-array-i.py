class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        neg_turnarounds = []
        pos_turnarounds = []
        cur = 1
        dir = 1
        n = len(nums)
        while cur < n:
            if nums[cur] == nums[cur -1]:
                return False
            elif nums[cur] < nums[cur-1] and dir > 0:
                if cur == 1:
                    return False
                neg_turnarounds.append(cur)
                dir = -1
            elif nums[cur] > nums[cur -1] and dir < 0:
                pos_turnarounds.append(cur)
                dir = 1
            cur += 1
        return len(neg_turnarounds) == 1 and len(pos_turnarounds) == 1