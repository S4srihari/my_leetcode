class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            for i in range(1,num):
                if i | (i+1) == num:
                    ans.append(i)
                    break
                elif i == num-1:
                    ans.append(-1)
                    break
        return ans