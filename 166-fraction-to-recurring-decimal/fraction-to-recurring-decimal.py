class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        num, den = abs(numerator), abs(denominator)
        if num == 0 : return "0"
        res = "-" if (numerator < 0)^(denominator < 0) else ""
        q = int(num/den)
        res += str(q)
        if q*den == num : return res
        num %= den
        res += "."
        cache = {}
        pos = 1 
        while True:
            if num in cache: break
            cache[num] = pos
            pos += 1
            num *= 10
            q = int(num/den)
            res += str(q)
            if q*den == num: return res
            num %= den
        l = pos - cache[num] + 1
        res = res[:-l+1] + "(" + res[-l+1:] + ")"
        return res