class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curSum = 0, maxSum = -INT_MAX; 
        for(int num : nums){
            curSum += num;
            if (maxSum < curSum) maxSum = curSum;
            if (curSum < 0) curSum = 0;
        }
        return maxSum;
    }
};