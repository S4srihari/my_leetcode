class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str2)
        idx = 0
        for ch in str1:
            if ch == str2[idx] or chr(ord(ch)+1) ==str2[idx] or (ch == "z" and str2[idx] == "a"):
                idx += 1
                if idx == n:
                    return True
        return False
        