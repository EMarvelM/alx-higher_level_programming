#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2]) {
  console.log(argv.splice(2).sort().slice(-2)[0]);
} else {
  console.log(0);
}
