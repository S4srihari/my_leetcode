/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let res = 0, temp = 0;
    let left = 0, right = height.length-1;
    while(left < right){
        if (height[left] <= height[right]){
            temp = height[left]*(right-left);
            left++;
        }
        else {
            temp = height[right]*(right-left);
            right--;
        }
        if(res < temp) res = temp;
    }
    return res;
};