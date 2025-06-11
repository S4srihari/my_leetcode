class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashset = set(nums)
        ans = []
        for i in range(1,len(nums)+1):
            if i not in hashset:
                ans.append(i)
        return ans