#!/usr/bin/node
/*
 * Prints messaage depending on no of arguments passed
 * Usage: ./2-arguments.js <arg1> <arg2> ...
 * Prints:
 *   - If no arguments passed: "No argument"
 *   - If one argument passed: "Argument found"
 *   - If more than one argument passed: "Arguments found"
 */
if (process.argv.length <= 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
