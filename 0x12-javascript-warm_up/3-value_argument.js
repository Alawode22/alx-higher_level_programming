#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else if (process.argv.length > 2) {
  console.log(process.argv[2]);
}
