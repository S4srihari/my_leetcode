class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        store = [0]*value
        for i in nums:
            if i >= 0:
                store[i%value] += 1
            else:
                store[(value-(abs(i)%value))%value] += 1
        res = 0
        while True:
            if not store[res%value]:
                break
            else:
                store[res%value] -= 1
                res += 1
        return res