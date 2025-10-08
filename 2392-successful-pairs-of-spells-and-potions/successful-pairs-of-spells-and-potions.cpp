class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(), potions.end());
        vector<int> ans;
        int m = potions.size();
        for (int i: spells){
            int c = (potions.end()-lower_bound(potions.begin(), potions.end(), (success+i-1)/i));
            ans.push_back(c);
        }
        return ans;
    }
};