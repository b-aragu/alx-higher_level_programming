#!/usr/bin/node
/*
 * 10-factorial.js
 * Prints the factorial of the first argument 
 * use recursion
 * usage: ./10-factorial.js <number>
 */

function factorial (n) {
  if (n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
if (process.argv.length <= 2) {
  console.log(1);
}
else {
  console.log(factorial(parseInt(process.argv[2])));
}
