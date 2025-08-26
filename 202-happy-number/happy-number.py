class Solution:
    def cal(self,n):
        ans = 0
        while n:
            ans += (n%10)**2
            n //= 10
        return ans

    def isHappy(self, n: int) -> bool:
        hashStore = set()
        res = self.cal(n)
        while res != 1:
            if res in hashStore:
                return False
            else:
                hashStore.add(res)
                res = self.cal(res)
        return True