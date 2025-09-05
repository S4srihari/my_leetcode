class Solution {
public:
    int makeTheIntegerZero(int num1, int num2) {
        long long n1 = num1;
        long long n2 = num2;   
        for (int k = 1; k <= 60; k++) {
            long long x = n1 - n2 * k;  
            if (x < 0) continue;
            if (__builtin_popcountll(x) <= k && x >= k) {
                return k;
            }
        }
        return -1;
    }
};