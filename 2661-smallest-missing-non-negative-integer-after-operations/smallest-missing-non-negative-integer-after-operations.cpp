class Solution {
public:
    int findSmallestInteger(vector<int>& nums, int value) {
        int n = nums.size();
        vector<int> arr(value, 0);
        for (int num: nums){
            if (num >= 0) arr[num%value]++;
            else arr[(value-std::abs(num)%value)%value]++;
        }
        int min_reps = n+1;
        int min_idx = -1;
        for (int idx=0; idx<value; idx++){
            if (arr[idx]<min_reps){
                min_reps = arr[idx];
                min_idx = idx;
            }
        }
        return min_reps*value + min_idx;
    }
};