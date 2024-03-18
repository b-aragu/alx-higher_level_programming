#!/usr/bin/node
/*
 * 11-second_biggest.js
 * Search for the second biggest number in a list of arguments
 * Usage: ./11-second_biggest.js <arguments>
 */
if (process.argv.length <= 2 || process.argv.length === 1) {
  console.log(0);
} else {
  let max = 0;
  let second = 0;
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > max) {
      second = max;
      max = process.argv[i];
    } else if (process.argv[i] > second) {
      second = process.argv[i];
    }
  }
  console.log(second);
}
