#!/usr/bin/node

function secBiggest (arr) {
  let max = 0;
  let res = 0;

  for (const value of arr) {
    const num = Number(value);

    if (num > max) {
      [res, max] = [max, num];
    } else if (num < max && num > res) {
      res = num;
    }
  }

  return res;
}

console.log(secBiggest(process.argv));
