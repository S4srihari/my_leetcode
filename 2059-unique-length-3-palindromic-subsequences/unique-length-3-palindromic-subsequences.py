class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        chars = set(s)
        res = 0
        for ch in chars:
            lidx = s.find(ch)
            ridx = s.rfind(ch)

            if ridx > lidx + 1:
                res += len(set(s[lidx+1:ridx]))
        return res