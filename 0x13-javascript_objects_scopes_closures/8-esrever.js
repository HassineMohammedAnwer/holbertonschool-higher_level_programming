#!/usr/bin/node
exports.esrever = function (list) {
  const desreverl = [];
  for (let i = list.length - 1; i >= 0; i--) {
    desreverl.push(list.pop());
  }
  return desreverl;
};
