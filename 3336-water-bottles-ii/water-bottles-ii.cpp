class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        int cnt = 0;
        while(numBottles >= numExchange){
            cnt += numExchange;
            numBottles -= numExchange;
            numExchange += 1;
            numBottles += 1;
        }
        return cnt + numBottles;
    }
};