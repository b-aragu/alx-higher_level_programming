#!/usr/bin/node
// 3-value_argument.js
/*
 * Prints messaage depending on value of argument passed
 * Usage: ./3-value_argument.js <arg>
 * Prints:
 *   - If no argument passed: "No argument" 
 *   - prints value if argument present
 */
if (process.argv.length <= 2) {
  console.log('No argument');
}
else{
  console.log(process.argv[2]);
}

