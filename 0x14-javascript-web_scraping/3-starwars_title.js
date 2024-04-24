#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const id = argv[2];
const url = "https://swapi-api.alx-tools.com/api/films/" + id;


request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
