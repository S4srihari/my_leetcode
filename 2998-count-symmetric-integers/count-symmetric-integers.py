class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for num in range(low, high+1):
            s = str(num)
            l = len(s)

            if l%2 == 0:
                half = l//2
                if sum(int(i) for i in s[:half]) == sum(int(i) for i in s[half:]):
                    res += 1
        return res