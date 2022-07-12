#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number);
  const len = process.argv.length;
  args.slice(2, len);
  args.sort(function (a, b) { return a - b; });
  console.log(args[len - 2]);
}
