class Solution {
public:
    int helper(int i, vector<int>& energy, int k){
        if (i<0) return 0;
        int prev = helper(i-k, energy, k);
        if (prev > 0) return energy[i] + prev;
        else return energy[i];
    }

    int maximumEnergy(vector<int>& energy, int k) {
        int n = energy.size();
        int val, res = INT_MIN;
        for (int i= n-1; i>n-1-k; i--){
            if (i >= 0){
                val = helper(i, energy, k);
            }
            else{
                break;
            }
            res = std::max(res, val);
        }
        return res;
    }
};