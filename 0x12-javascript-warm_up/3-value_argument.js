#!/usr/bin/node

const { argv } = require('process');
let i = 0;
argv.forEach((val, index) => {
  i++;
});
if (i <= 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
