/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const res = [];
    let idx =0;
    for (const num in arr) {
        res.push(fn(arr[idx], idx));
        idx++;
        }
    return res;
};