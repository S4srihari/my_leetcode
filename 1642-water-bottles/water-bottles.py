class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt, bonus = 0,0
        while(numBottles >= numExchange):
            bonus = numBottles//numExchange
            cnt += bonus*numExchange
            numBottles = (numBottles % numExchange) + bonus 
        return cnt+numBottles