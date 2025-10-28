class Solution {
public:
    int countValidSelections(vector<int>& nums) {
        int tot = 0, res = 0, leftSum = 0;
        for (int num: nums) tot += num;
        for (int num: nums){
            if (num == 0){
                if (leftSum == tot-leftSum) res += 2;
                else if (std::abs(leftSum - (tot-leftSum)) == 1) res++;
            }
            leftSum += num;
        }
        return res;
    }
};