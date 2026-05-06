#!/usr/bin/node

const myInt = parseInt(process.argv[2]);

if (isNaN(myInt)) {
  console.log("Missing number of occurrences");
} else {
  for (let i = 0; i < myInt; i++) {
    console.log("C is fun");
  }
}
