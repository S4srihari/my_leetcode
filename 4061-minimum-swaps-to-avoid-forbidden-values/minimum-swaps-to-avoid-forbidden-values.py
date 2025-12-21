class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        for num in forbidden:
            freq[num] += 1
        for i in freq:
            if freq[i] > n:
                return -1
        badpairs = defaultdict(int)
        for i,num in enumerate(nums):
            if num==forbidden[i]:
                badpairs[num] += 1
        if not badpairs:
            return 0
        maxi = max(badpairs.values())
        total = sum(badpairs.values())
        return max((total+1)//2, maxi)