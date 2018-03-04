#!/usr/local/bin/node

"use strict";

const count = 10000;

let list = [];
for (let i = 2; i < count; i++) {
  let divs = divisors(i);
  if (divs.length > 0) {
    list[i] = divisors(i).reduce((total, val) => total + val);
    //console.log(`${i}: ${list[i]}`);
  }
}
let sum = 0;
for (let i = 2; i < count; i++) {
  let n = list[i];
  if (i != n && i == list[n]) {
    sum += n + i;
    console.log(`${i},${n}: ${list[i]}`);
  }
}
// Numbers appeared in pairs, so we divide by two.
console.log(sum / 2);

function divisors(n) {
  let divs = []; 
  // Simple efficiency.  Fast enough so not bothering to refine.
  let max = n / 2 + 1;
  for (let j = 1; j < max; j++) {
    if (n % j == 0) {
      divs.push(j);
    }
  }
  //console.log(divs);
  return divs;
}
