#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2]) {
  console.log(argv.splice(2).sort().slice(-2)[0]);
} else if (!isNaN(Number(argv[2]))) {
console.log(0);
}
