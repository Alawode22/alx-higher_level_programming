#!/usr/bin/node
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);
if (arg1 === undefined || isNaN(arg1)) {
  console.log('NaN');
} else {
  console.log(arg1 + arg2);
}
