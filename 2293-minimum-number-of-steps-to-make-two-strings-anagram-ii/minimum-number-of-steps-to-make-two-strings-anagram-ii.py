class Solution:
    def minSteps(self, s: str, t: str) -> int:
        arr = [0]*26
        for c in s:
            arr[ord(c)-ord('a')] += 1
        for c in t:
            arr[ord(c)-ord('a')] -= 1
        res = 0
        for i in arr:
            res += abs(i)
        return res