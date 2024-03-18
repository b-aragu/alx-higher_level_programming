#!/usr/bin/node
/*
 * 10-factorial.js
 * Prints the factorial of the first argument
 * usage: ./10-factorial.js <number>
 */

if (!isNaN(process.argv[2])) {
  const num = parseInt(process.argv[2]);
  let fact = 1;
  for (let i = 1; i <= num; i++) {
    fact *= i;
  }
  console.log(fact); 
}
else{
  console.log(1);
}
