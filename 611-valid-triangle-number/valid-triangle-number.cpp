class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int cnt = 0, n = nums.size();
        sort(nums.begin(),nums.end());
        for (int i=0; i<n-2; i++){
            if (nums[i] <= 0) continue;
            for(int j=i+1; j<n-1; j++){
                auto val = std::upper_bound(nums.begin(), nums.end(), nums[i]+nums[j]-1);
                int idx = std::distance(nums.begin(), val);
                cnt += idx-j-1;
            }
        }
        return cnt;
    }
};