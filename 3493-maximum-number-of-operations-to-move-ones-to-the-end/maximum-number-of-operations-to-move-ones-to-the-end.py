class Solution:
    def maxOperations(self, s: str) -> int:
        res = 0
        setBits = 0
        for i in range(len(s)):
            if s[i] == '1': setBits += 1
            else:
                if i > 0 and s[i-1] == '1':
                    res += setBits
        return res