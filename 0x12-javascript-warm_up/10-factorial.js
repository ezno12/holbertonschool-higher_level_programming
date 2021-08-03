#!/usr/bin/node

function fact (num) {
  if (num === 0) {
    return 1;
  }
  return num * fact(num - 1);
}
console.log(fact(parseInt(process.argv[2])));
