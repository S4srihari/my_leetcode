class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1,n):
            if not "0" in str(a) and not "0" in str(n-a):
                return [a,n-a]
        return [-1,-1]