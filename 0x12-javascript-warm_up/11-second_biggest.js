#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length < 4) {
  console.log(0);
} else {
  // get largest number
  let largest = Number(argv[2]);
  let smallest = Number(argv[2]);
  argv.forEach((word) => {
    if (!(isNaN(Number(word)))) {
      // write condition to check for the largest number
      if (largest < Number(word)) {
        largest = Number(word);
      }
      if (smallest > Number(word)) {
        smallest = Number(word);
      }
    }
  });

  // get the second largest number
  for (let i = 0; i < argv.length; i++) {
    if (!(isNaN(Number(argv[i])))) {
      if (Number(argv[i]) < largest && smallest < Number(argv[i])) {
        smallest = Number(argv[i]);
      }
    }
  }

  // print the second largest number
  console.log(smallest);
}
