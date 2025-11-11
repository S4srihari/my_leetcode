/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const filteredArr = [];
    let i = 0
    for (const num of arr){ 
        if( fn(num,i)){
        filteredArr.push(num);
        }
        i++;
    }
    return filteredArr;
};