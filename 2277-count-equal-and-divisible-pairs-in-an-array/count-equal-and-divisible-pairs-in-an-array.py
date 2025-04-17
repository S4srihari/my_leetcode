class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        freq = {}
        for i in range(n):
            if nums[i] in freq:
                for j in freq[nums[i]]:
                    if (i*j)%k == 0:
                        cnt += 1
                freq[nums[i]].append(i)
            else :
                freq[nums[i]] = [i]
        return cnt