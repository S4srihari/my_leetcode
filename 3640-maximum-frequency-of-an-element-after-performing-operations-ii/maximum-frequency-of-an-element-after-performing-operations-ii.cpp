class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        sort(nums.begin(), nums.end());
        unordered_map<int, int> hash;
        for (int num: nums) hash[num]++;
        int res = 0, n = nums.size();
        for (pair<int, int> ele : hash){
            int j = ele.first;
            vector<long long> targets = {j, j + k, j - k};
            for (long long i : targets){
                int freq = 0;
                if (hash.count(i)) freq = hash[(int)i];
                auto left = lower_bound(nums.begin(), nums.end(), i-k);
                auto right = upper_bound(nums.begin(), nums.end(), i+k);
                int dist = std::distance(left, right);
                int cur = std::min(dist, freq + numOperations);
                res = std::max(res, cur);
            }
        }
        return res;
    }
};