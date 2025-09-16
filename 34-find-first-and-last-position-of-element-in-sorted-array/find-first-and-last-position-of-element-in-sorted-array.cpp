class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res(2,-1);
        int left = 0, right = nums.size()-1;
        while (left <= right){
            int mid = left + (right-left)/2;
            if(nums[mid] == target) {
                res[0] = mid;
            }
            if(nums[mid]>=target) right = mid-1;
            else left = mid+1;
        }
        left = 0; 
        right = nums.size()-1;
        while (left <= right){
            int mid = left + (right-left)/2;
            if(nums[mid] == target) {
                res[1] = mid;
            }
            if(nums[mid]<=target) left = mid+1;
            else right = mid-1;
        }
        return res;
    }
};