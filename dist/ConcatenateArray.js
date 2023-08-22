"use strict";
function getConcatenation(nums) {
    let size = nums.length;
    let ans = [];
    for (let index = 0; index < size; index++) {
        ans[index] = nums[index];
    }
    ans.forEach((num) => ans.push(num));
    return ans;
}
getConcatenation([1, 2, 3]);
