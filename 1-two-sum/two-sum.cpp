class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> hash;
        for (int i=0; i<nums.size(); i++){
            if (hash.count(nums[i])) return {hash[nums[i]],i};
            hash[target-nums[i]] = i;
        }
        return {-1,-1};
    }
};