class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int cnt = 0, n = nums.size();
        sort(nums.begin(),nums.end());
        for(int i=n-1; i>1; i--){
            int r=i-1;
            int l=0;
            while(l<r){
                int sum=nums[l]+nums[r];
                if(sum>nums[i]){
                    cnt += r-l;
                    r--;
                }else{
                   l++;
                }
            }
        }
        return cnt;
    }
};