#!/usr/bin/node
/*
 * Prints messaage depending on value of argument passed
 * Usage: ./3-value_argument.js <arg>
 * Prints:
 *   - If no argument passed: "No argument" 
 *   - prints value if argument present
 */

if (process.argv !== undefined) {
  console.log(process.argv[2]);
}else{
  console.log('No argument');
}

