#!/usr/bin/node
const { argv } = require('node:process');

const n = factorial(Number(argv[2]));
console.log(n);

function factorial (n) {
    if (n < 2) {
        return (n);
    }
    return n *= factorial(n - 1);
}