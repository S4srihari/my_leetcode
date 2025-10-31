class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        cnt = 2
        zeroVisited = set()
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0 or abs(nums[i]) in zeroVisited:
                res.append(abs(nums[i]))
                cnt -= 1
            else:
                if nums[abs(nums[i])] > 0:
                    nums[abs(nums[i])] *= -1
                else:
                    zeroVisited.add(abs(nums[i]))

        return res + [0]*cnt