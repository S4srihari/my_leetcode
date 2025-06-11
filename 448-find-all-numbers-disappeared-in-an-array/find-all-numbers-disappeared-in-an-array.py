class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n_hash = defaultdict(int)
        ans = []
        for num in nums:
            n_hash[num] = 1
        for i in range(1,len(nums)+1):
            if i not in n_hash:
                ans.append(i)
        return ans