"use strict";
function containsDuplicate(nums) {
    const check = new Set(nums);
    return check.size < nums.length;
}
const nums = [1, 2, 3, 4, 5];
containsDuplicate(nums);
