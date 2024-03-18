#!/usr/bin/node
/*
 * call_me_moby
 * executes x times a function
 */

exports.callMeMoby = function callMeMoby (x, func) {
  for (let i = 0; i < x; i++) {
    func();
  }
}
