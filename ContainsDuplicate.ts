function containsDuplicate(nums: number[]): boolean {
  const check = new Set<number>(nums);

  return check.size < nums.length;
}

const nums = [1, 2, 3, 4, 5];
containsDuplicate(nums);
