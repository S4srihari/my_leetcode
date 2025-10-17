class Solution:
    def minSteps(self, s: str, t: str) -> int:
        arr = [0]*26
        for c in s:
            arr[ord(c)-ord('a')] += 1
        for c in t:
            arr[ord(c)-ord('a')] -= 1
        res = 0
        for i in range(26):
            res += abs(arr[i])
        return res