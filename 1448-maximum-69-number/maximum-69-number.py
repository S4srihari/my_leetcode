class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        for idx in range(len(s)):
            if s[idx] == "6":
                s = s[:idx] + "9" + s[idx+1:]
                break
        return int(s)
