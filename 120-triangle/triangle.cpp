class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<int> ahead(n+1,0), cur(n+1,0);
        for (int i=n-1; i>-1; i--){
            for (int j=i; j>-1; j--){
                cur[j] = std::min(ahead[j],ahead[j+1]) + triangle[i][j];
            }
            ahead = cur;
        }
        return ahead[0];
    }
};