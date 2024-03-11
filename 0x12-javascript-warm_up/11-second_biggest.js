#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const myList = process.argv.slice(2).map(Number);
  const result = myList.sort((a, b) => b - a)[1];
  console.log(result);
}
