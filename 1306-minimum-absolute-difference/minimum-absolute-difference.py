class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        if n < 2:
            return []
        nums = sorted(arr)
        diff = nums[1] - nums[0]
        res = [[nums[0], nums[1]]]
        for i in range(1,n-1):
            if nums[i+1] - nums[i] < diff:
                diff = nums[i+1] - nums[i]
                res = [[nums[i], nums[i+1]]]
            elif nums[i+1] - nums[i] == diff:
                res.append([nums[i],nums[i+1]])
        return res