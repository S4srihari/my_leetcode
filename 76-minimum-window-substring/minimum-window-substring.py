class Solution:
    def substr(self, f1, f2):
        for key, val in f1.items():
            if f2[key] < val:
                return False
        return True
        
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m:
            return ""
        freq, freq2 = defaultdict(int), defaultdict(int)
        for idx in range(n):
            freq[t[idx]] += 1
            freq2[s[idx]] += 1
        if self.substr(freq,freq2):
            return s[:n]
        left,right = 0,n
        ans = ""
        while right < m :
            freq2[s[right]] += 1
            if self.substr(freq,freq2):
                while self.substr(freq,freq2):
                    freq2[s[left]] -= 1
                    left += 1
                if len(ans) >= right - left + 2 or ans == "":
                    ans = s[left-1:right+1]
            right += 1
        return ans