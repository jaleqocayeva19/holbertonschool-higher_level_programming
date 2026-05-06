#!/usr/bin/node

const arr = [
  "C is fun",
  "Python is cool",
  "JavaScript is amazing"
];

let result = "";

for (let i = 0; i < arr.length; i++) {
  result = result + arr[i] + "\n";
}

console.log(result);
