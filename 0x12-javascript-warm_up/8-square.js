#!/usr/bin/node

const arg = process.argv[2];
let i;
if (isNaN(arg) === true) {
  console.log('Missing size');
} else {
  for (i = 0; i < arg; i++) {
    console.log('X'.repeat(arg));
  }
}
