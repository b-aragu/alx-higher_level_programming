#!/usr/bin/node
/*
 * 9-add.js
 * Prints the addition of 2 integers
 * Usage: ./9-add.js <int1> <int2>
 */
function add (a, b) {
  return (a + b);
}
console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
