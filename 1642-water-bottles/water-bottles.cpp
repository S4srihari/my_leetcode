class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        if(numExchange < 2) return -1;
        int cnt = 0, recycle = 0;
        while(numBottles >= numExchange){
            recycle = numBottles/numExchange;
            cnt += numExchange*recycle;
            numBottles = numBottles%numExchange + recycle;
        }
        cnt += numBottles;
        return cnt;
    }
};