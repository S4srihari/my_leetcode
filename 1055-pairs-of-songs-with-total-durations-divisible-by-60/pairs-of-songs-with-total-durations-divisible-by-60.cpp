class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        int arr[60] = {0};
        for (int t: time){
            arr[t%60]++;
        }
        int res = 0;
        for (int i=1; i<30; i++){
            res += arr[i]*arr[60-i];
        }
        if (arr[0]%2) res += arr[0]*(0.5*(arr[0]-1));
        else res += 0.5*arr[0]*(arr[0]-1);
        if (arr[30]%2) res += arr[30]*(0.5*(arr[30]-1));
        else res += 0.5*arr[30]*(arr[30]-1);
        return res;
    }
};