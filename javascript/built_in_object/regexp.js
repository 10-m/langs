// -*- coding: utf-8-unix -*-
"use strict";

const str = "I'm Bob. Tom is my friend.";

// Regexp object members
let reg = /.o./g;
console.log(reg.exec(str)); //[Bob]
console.log(reg.test(str)); //true

console.log(reg.toString(str)); ///.o./
console.log(reg.source); //.o.

console.log(reg.global); //true
console.log(reg.ignoreCase); //false
console.log(reg.multiline); //false

// Get all matched result
const str2 = "I'm Bob. Tom is my friend.";
let reg2 = /.o./g;
let result;

// by exec
while(result = reg2.exec(str2)) {
  console.log('%s, lastIndex:%s', result[0], reg2.lastIndex);
}

// by match
console.log(str.match(reg2)); //[Bob, Tom]
let reg3 = /.o./;
console.log(str.match(reg3)); //[Bob]

// Replace
let reg4 = /.o./g;
console.log(str.replace(reg4, 'Jay')); //I'm Jay. Jay is my friend.

// Split
const date = '2017/09/06 09:48:15';

let reg5 = /[:\/\s]/g;
console.log(str.split(reg5)); //[I'm, Bob., Tom, is, my, friend.]
console.log(date.split(reg5)); //[2017, 09, 06, 09, 48, 15]
