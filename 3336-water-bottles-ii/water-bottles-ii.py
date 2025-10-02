class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        cnt = 0
        while numBottles >= numExchange:
            cnt += numExchange
            numBottles -= numExchange
            numBottles += 1
            numExchange += 1
        return cnt + numBottles