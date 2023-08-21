function isAnagram(s: string, t: string): boolean {
  let check: boolean = true;

  if (s.length === t.length) {
    let s_sorted = s.split("").sort().join("");
    let t_sorted = t.split("").sort().join("");

    for (let index = 0; index < s_sorted.length; index++) {
      if (s_sorted.charAt(index) !== t_sorted.charAt(index)) {
        check = false;
      }
    }
  } else {
    check = false;
  }

  return check;
}

console.log(isAnagram("rat", "tar"));
