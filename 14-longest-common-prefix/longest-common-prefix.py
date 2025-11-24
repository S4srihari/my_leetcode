class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur = [i for i in strs[0]]
        for word in strs:
            if not cur:
                return ""
            idx = 0
            for i in range(min(len(cur),len(word))):
                if word[i] != cur[i]:
                    break
                idx += 1
            cur = cur[:idx]
        return "".join(cur)