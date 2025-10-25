class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n//7
        res = (weeks*28) + (7*((weeks*(weeks-1))//2))
        days = n%7
        res += (days*(weeks+1)) + (days*(days-1)//2)
        return res