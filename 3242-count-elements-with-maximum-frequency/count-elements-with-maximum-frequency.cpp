class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        int res =0, maxi =0;
        unordered_map<int,int> map;
        for (int num : nums){
            map[num]++;
            if (map[num] == maxi) res += maxi;
            else if (map[num] > maxi) {
                maxi = map[num];
                res = maxi;
            }
            else continue;
        }
        return res;
    }
};