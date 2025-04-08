class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        distinct = {}
        edge = 0
        for i in range(len(nums)):
            if nums[i] in distinct :
                edge = max(distinct[nums[i]]+1,edge)
            distinct[nums[i]] = i
        return edge//3 if edge%3 == 0 else edge//3 +1