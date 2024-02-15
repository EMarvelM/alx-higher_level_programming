#!/usr/bin/node
const { argv } = require('node:process');

let num = Number(argv[2]);
if (isNaN(num))
{
	num = 1;
	console.log(num)
} else {
  // calculate factorial
  num = factor(num);
  console.log(num);
}

function factor(n) {
  if (n < 1) {
    return 1;
  }
  let num = n - 1;
  let ret;
  ret = factor(num);
  return Number(n * ret);
}
