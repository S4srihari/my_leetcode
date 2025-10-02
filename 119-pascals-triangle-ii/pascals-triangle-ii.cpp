class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> prev(2,1), cur(1,1);
        if (rowIndex == 0) return cur;
        else if (rowIndex == 1) return prev;
        for (int i=2; i<=rowIndex; i++){
            cur = {1};
            for (int j=0; j<i-1; j++){
                cur.push_back(prev[j]+prev[j+1]);
            }
            cur.push_back(1);
            prev = cur;
        }
        return prev;
    }
};