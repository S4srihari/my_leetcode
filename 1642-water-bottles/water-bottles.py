class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numExchange < 2: return -1
        cnt, bonus = 0,0
        while(numBottles >= numExchange):
            bonus = numBottles//numExchange
            cnt += bonus*numExchange
            numBottles = (numBottles % numExchange) + bonus 
        return cnt+numBottles