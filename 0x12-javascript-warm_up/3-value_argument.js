#!/usr/bin/node
if (process.argv !== undefined) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
