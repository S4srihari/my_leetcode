class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        dic = set()
        substr, long_substr = 0, 0
        for right in range(len(s)):
            if s[right] not in dic:
                dic.add(s[right])
                substr = right - left + 1
                long_substr = max(substr, long_substr)
                continue
            while s[right] != s[left]:
                dic.remove(s[left])
                left += 1
            left += 1
        return long_substr