class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        """freqMap = Counter(nums)
        hashSet = set()
        for ele in sorted(freqMap.keys()):
            val = freqMap[ele]
            diff = -k
            while diff <= k and val > 0:
                if ele+diff not in hashSet:
                    hashSet.add(ele+diff)
                    val -= 1
                diff += 1
        return len(hashSet)"""
        if not nums : return 0
        nums.sort()
        nums[0] -= k
        res = 1
        cur = nums[0]
        for i in range(1,len(nums)):
            if nums[i] + k > cur:
                nums[i] = max(cur+1, nums[i]-k)
                res += 1
                cur = nums[i]
                print(cur)
        return res
            