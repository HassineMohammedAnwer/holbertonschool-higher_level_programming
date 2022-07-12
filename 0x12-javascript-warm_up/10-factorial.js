#!/usr/bin/node

let res = 1;
if (isNaN(process.argv[2]) || (process.argv[2] == 0)) {
  console.log(1);
  return;
} else {
  for (let i = 1; i <= parseInt(process.argv[2]); i++) {
    res = res * i;
  }
}
console.log(res);
