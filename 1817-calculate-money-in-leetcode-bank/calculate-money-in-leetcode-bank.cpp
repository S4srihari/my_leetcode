class Solution {
public:
    int totalMoney(int n) {
        int weeks = n/7, days = n%7;
        int res = weeks*28 + (weeks*(weeks-1)/2)*7;
        res += days*(weeks+1) + days*(days-1)/2;
        return res;
    }
};