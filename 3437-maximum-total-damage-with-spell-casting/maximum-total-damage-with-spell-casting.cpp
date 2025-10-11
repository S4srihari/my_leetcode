class Solution {
public:
    long long maximumTotalDamage(vector<int>& power) {
        unordered_map<int,int> Freq;
        for (int d: power) Freq[d]++;
        int n = 0;
        vector<int> vals;
        for (auto [k,v]: Freq){
            n++;
            vals.push_back(k);
        }
        if (n==0) return 0;
        sort(vals.begin(), vals.end());
        vector<long long> totals;
        for (int i=0; i<n; i++){
            totals.push_back(1LL*vals[i]*Freq[vals[i]]);
        }
        vector<long long> dp(n,0);
        dp[0] = totals[0];
        long long prev, no_prev;
        int j;
        for (int idx=1; idx<n; idx++){
            no_prev = std::max(dp[idx-1],totals[idx]);
            prev = 0;
            j = idx-1;
            while (j>=0 && vals[idx]-vals[j]<=2) j--;
            if (j != -1){
                prev = dp[j] + totals[idx];
            }
            dp[idx] = std::max(prev, no_prev);
        }
        return dp[n-1];
    }
};