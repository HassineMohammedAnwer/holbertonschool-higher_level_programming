#!/usr/bin/node
let x = process.argv[2];
function factorial (x) {
  let res = 1;
  if (isNaN(x) || (x == 0)) {
    return (1);
  } else {
    for (let i = 1; i <= parseInt(x); i++) {
      res = res * i;
    }
}
  return (res);
}
console.log(factorial(x));
