/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const res = [];
    const len = arr.length;
    for (let idx =0; idx < len; idx++) {
        res[idx] = fn(arr[idx], idx);
        }
    return res;
};