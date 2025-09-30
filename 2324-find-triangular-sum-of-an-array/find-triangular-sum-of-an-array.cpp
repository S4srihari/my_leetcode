class Solution {
public:
    int triangularSum(vector<int>& nums) {
        vector<int> prev = nums, cur;
        while(prev.size()>1){
            for(int i=1; i<prev.size(); i++){
                cur.push_back((prev[i]+prev[i-1])%10);
            }
            prev = cur;
            cur.clear();
        }
        return prev[0];
    }
};