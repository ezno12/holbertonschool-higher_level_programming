#!/usr/bin/node

const SquareOld = require('./5-square.js');
module.exports = class Square extends SquareOld {
  charPrint (c) {
    if (c === undefined) {
      return this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
