class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m:
            return ""
        freq = defaultdict(int)
        for idx in range(n):
            freq[t[idx]] += 1
        chars_rem = n
        left = 0
        ans = [0,float("inf")]
        for right, char in enumerate(s):
            if char in freq and freq[char] > 0:
                chars_rem -= 1
            freq[char] -= 1
            if chars_rem == 0:
                while True:
                    if freq[s[left]] == 0:
                        break
                    freq[s[left]] += 1
                    left += 1
                if ans[1]-ans[0] > right - left:
                    ans = [left, right+1]
                freq[s[left]] += 1
                left += 1
                chars_rem += 1
            right += 1
        return s[ans[0]:ans[1]] if ans[1] != float("inf") else ""