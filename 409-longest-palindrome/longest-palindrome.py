class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        l = 0
        m = 0
        for i in c:
            if c[i]%2 == 0:
                l += c[i]
            else :
                m = 1
                l += (c[i]-1)
        
        return l + m