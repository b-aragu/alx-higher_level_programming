#!/usr/bin/node
/*
 * 7-multi_c.js
 * Prints 'X' times "C is fun"
 * X is the first arguement passed to the script
 */
if (process.argv.length === 3) {
  const X = parseInt(process.argv[2]);
  for (let i = 0; i < X; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
