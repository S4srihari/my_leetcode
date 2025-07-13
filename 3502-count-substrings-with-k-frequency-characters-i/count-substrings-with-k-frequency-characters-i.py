class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        total = 0
        n = len(s)
        """for i in range(n-k+1):
            freq = [0]*26
            for j in range(i,n):
                freq[ord(s[j])-ord("a")] += 1
                if freq[ord(s[j])-ord("a")] >= k:
                    total += n-j
                    break"""
        freq = [0]*26
        l = 0
        for r in range(n):
            idx = ord(s[r])-ord("a")
            freq[idx] += 1
            while freq[idx] >= k:
                total += n-r
                freq[ord(s[l])-ord("a")] -= 1
                l += 1
        return total