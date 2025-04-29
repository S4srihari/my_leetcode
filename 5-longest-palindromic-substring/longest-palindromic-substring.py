class Solution:
    def longestPalindrome(self, s: str) -> str:
        """ans = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i:j+1] == s[i:j+1][::-1] and len(ans) < j+1-i:
                    ans = s[i:j+1]
        return ans"""

        if not s :
            return ""
        ans = ""
        max_len = 0
        def expanding(s, i, j):
            while i >= 0 and j < len(s) and s[i] == s[j] :
                i -= 1
                j += 1
            return j-i-1
        
        for i in range(len(s)):
            odd = expanding(s,i,i)
            even = expanding(s,i,i+1)
            maxi = max(odd,even)
            print(maxi)

            if maxi > max_len :
                max_len = maxi
                diff = maxi//2
                if maxi % 2 != 0:
                    ans = s[i-diff:i+diff+1]
                else :
                    ans = s[i-diff+1:i+diff+1]
        return ans