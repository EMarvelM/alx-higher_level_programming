#!/usr/bin/node
const { argv } = require('node:process');
if (!argv[2]) {
  console.log(1);
} else {
  const n = factorial(Number(argv[2]));
  console.log(n);
}

function factorial (n) {
  if (n < 2) {
    return (n);
  }
  n *= factorial(n - 1);
  return (n);
}
