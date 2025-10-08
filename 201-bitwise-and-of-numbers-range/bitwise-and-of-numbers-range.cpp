class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        if (left < 0 || right < 0) return -1;
        int cnt = 0;
        while(left != right){
            left >>= 1;
            right >>= 1;
            cnt++;
        }
        return (left << cnt);
    }
};