class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str2)
        idx = 0
        for ch in str1:
            if (ord(str2[idx])-ord(ch))%26< 2:
                idx += 1
                if idx == n:
                    return True
        return False
        