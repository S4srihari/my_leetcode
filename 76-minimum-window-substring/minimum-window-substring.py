class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        chars = {}
        for char in t:
            chars[char] = chars.get(char,0) + 1

        chars_rem = len(t)
        l = 0
        min_window = (0, float("inf"))
        for idx, char in enumerate(s):
            if char in chars and chars[char] > 0:
                chars_rem -= 1
            chars[char] = chars.get(char,0) - 1

            if chars_rem == 0:
                while True:
                    char = s[l]
                    if chars[char] == 0:
                        break
                    chars[char] += 1
                    l += 1
                
                if idx - l < min_window[1] - min_window[0]:
                    min_window = (l,idx)
                
                chars[s[l]] += 1
                l += 1
                chars_rem += 1

        return "" if min_window[1] > len(s) else "".join(s[min_window[0]:min_window[1]+1])