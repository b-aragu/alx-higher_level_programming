#!/usr/bin/node
/*
 * 8-square.js
 * prints a square using 'X'
 * usage: ./8-square.js <size>
 */
if (!isNaN(process.argv[2])){
  const size = parseInt(process.argv[2]);
  for (let i = 0; i < size; i++){
    console.log('X'.repeat(size));
  }
}
else{
  console.log("Missing size");
}
