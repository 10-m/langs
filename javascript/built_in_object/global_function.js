// -*- coding: utf-8-unix -*-
"use strict";

// global function
console.log(isFinite(123)); //true
console.log(isFinite('123')); //true
console.log(isFinite(Infinity)); //false
console.log(isFinite(NaN)); //false

console.log(isNaN(123)); //false
console.log(isNaN('123')); //false
console.log(isNaN(Infinity)); //false
console.log(isNaN(NaN)); //true

// URI eoncode / decode
let str = '字';
console.log(encodeURI(str));
console.log(encodeURIComponent(str));

let uri = 'https://www.google.co.jp/search?q=字';
console.log(encodeURI(uri));
console.log(encodeURIComponent(uri));
