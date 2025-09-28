class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        while (true){
            if (nums.size() < 3) return 0;
            int a = nums.back();
            nums.pop_back();
            int b = nums.back(); 
            nums.pop_back();
            int c = nums.back();
            nums.pop_back();
            if (a < b+c) return a+b+c;
            else {
                nums.push_back(c);
                nums.push_back(b);
            }
        }
    }
};