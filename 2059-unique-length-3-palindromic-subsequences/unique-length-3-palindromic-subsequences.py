class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1]*26
        last = [-1]*26
        for i, ch in enumerate(s):
            idx = ord(ch)-ord('a')
            if first[idx] == -1: first[idx] = i
            else: last[idx] = i
        
        res = 0
        for i in range(26):
            if last[i] - first[i] > 1:
                res += len(set([ch for ch in s[first[i]+1:last[i]]]))
        return res