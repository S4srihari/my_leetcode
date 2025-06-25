class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)

        def recurse(first, curr, nums):
            output.append(curr[:])
            for i in range(first,n):
                curr.append(nums[i])
                recurse(i+1, curr, nums)
                curr.pop()
            return
        
        recurse(0,[],nums)
        return output