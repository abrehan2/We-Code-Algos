function getConcatenation(nums: number[]): number[] {
  let size: number = nums.length;
  let ans: Array<number> = [];

  for (let index: number = 0; index < size; index++) {
    ans[index] = nums[index];
  }

  ans.forEach((num) => ans.push(num));

  return ans;
}

getConcatenation([1, 2, 3]);
