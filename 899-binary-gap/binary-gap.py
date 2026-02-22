class Solution:
    def binaryGap(self, n: int) -> int:
        binary_str = str(bin(n))
        res = 0
        cur = 0
        seen = False
        for i in range(len(binary_str)):
            if binary_str[i] == '1':
                res = max(res, cur)
                cur = 1
                seen = True
            elif seen:
                cur +=  1
        return res