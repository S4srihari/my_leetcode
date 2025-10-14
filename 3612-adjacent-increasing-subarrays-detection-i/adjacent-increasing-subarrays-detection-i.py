class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-k-k+1):
            valid = True
            for j in range(i+1,i+k):
                if nums[j] <= nums[j-1]:
                    valid = False
                    break
            if not valid: continue
            for j in range(i+k+1,i+k+k):
                if nums[j] <= nums[j-1]:
                    valid = False
                    break
            if valid : return True
        return False
