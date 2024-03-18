#!/usr/bin/node
/*
 * 102-add_me_maybe.js
 * function than increments and calls a function
 */

exports.addMeMaybe = function addMeMaybe (number, theFunction) {
  number = number + 1;
  theFunction(number);
};
