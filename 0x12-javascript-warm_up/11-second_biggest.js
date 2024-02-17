#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length < 4) {
  console.log(0);
} else {
  // get largest number
  let largest = Number(argv[2]);
  let word;
  argv.forEach((word)=> {
    if (!(isNaN(Number(word)))) {
      // write condition to check for the largest number
      if (largest < Number(word)) {
        largest =  Number(word);
      }
    }
  });

  // prrint the largest number
  console.log(largest);
}


// node program_name argv0 argv1
// ./pagram_name