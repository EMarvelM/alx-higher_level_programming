#!/usr/bin/node

const { argv } = require('node:process');
const { writeFile } = require('node:fs');

const file = argv[2];
const content = argv[3];

writeFile(file, content, (err) => {
  if (err) throw err;
});
