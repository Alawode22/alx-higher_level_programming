#!/usr/bin/node

const list = require('./100-data.js').list;
const map = list.map(x => x);
const map2 = list.map((x, index) => x * index);
console.log(map);
console.log(map2);
