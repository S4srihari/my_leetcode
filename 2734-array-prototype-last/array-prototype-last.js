/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
  if (this.length === 0){
    return -1;
  }
  let ans = this[this.length-1];
  return ans;
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */