class Solution:
    def extend(self,left,right,s):
        n = len(s)
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right-left-1

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        left,right = 0,0
        if len(s) == 1:
            return 1
        res = 0
        for idx in range(n):
            odd = self.extend(idx,idx,s)
            res += math.ceil(odd/2)
            even = self.extend(idx,idx+1,s)
            res += even//2
        return res