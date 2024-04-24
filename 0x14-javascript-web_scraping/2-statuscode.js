#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');

url = argv[2];
console.log(url);
if (!url) { process.exit(1); }

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  };
  console.log('code: ', response.statusCode);
})
