class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        startSet = set()
        n = len(s)
        res = 0
        for i in range(n-2):
            if s[i] in startSet:
                continue
            middleSet = set()
            temp = 0
            for j in range(i+1,n):
                if s[j] == s[i] and j > i+1:
                    temp = len(middleSet)
                    startSet.add(s[i])
                middleSet.add(s[j])
            res += temp
        return res