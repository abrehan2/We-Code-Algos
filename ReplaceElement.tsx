function replaceElements(arr: number[]): number[] {
  let currentMax = -1;

  for (let index: number = arr.length - 1; index >= 0; index--) {
    let newMax = Math.max(currentMax, arr[index]);
    arr[index] = currentMax;
    currentMax = newMax;
  }

  return arr;
}
replaceElements([1, 2, 3, 4, 5]);
