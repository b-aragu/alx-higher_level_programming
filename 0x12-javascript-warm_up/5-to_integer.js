#!/usr/bin/node
/*
 *  a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
 * usage: ./5-to_integer.js <number>
 */

if (!isNaN(process.argv[2])) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
