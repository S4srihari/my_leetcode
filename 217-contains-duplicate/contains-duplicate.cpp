class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> hash;
        for(int i : nums){
            if(hash.count(i)) return true;
            else hash.insert(i);
        }
        return false;
    }
};