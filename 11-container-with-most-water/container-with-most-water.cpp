class Solution {
public:
    int maxArea(vector<int>& height) {
        int area = 0, maxArea = 0;
        int left = 0, right = height.size()-1;
        while (left < right){
            if (height[left] <= height[right]){
                area = height[left]*(right-left);
                left++;
            }
            else {
                area = height[right]*(right-left);
                right--;
            }
            if (area > maxArea) maxArea = area;
        }
        return maxArea;
    }
};