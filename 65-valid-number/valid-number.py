class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        num = dot = exp = False

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = True

            elif ch in "+-":
                if i > 0 and s[i-1] not in "eE":
                    return False

            elif ch in "eE":
                if exp or not num:
                    return False
                exp = True
                num = False 

            elif ch == '.':
                if dot or exp:
                    return False
                dot = True

            else:
                return False

        return num
        