class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        stack = [-1]
        for num in nums:
            while stack[-1] > num:
                stack.pop()
            if stack[-1] < num:
                res += 1 if num > 0 else 0
                stack.append(num)
        return res
