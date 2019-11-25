// -*- coding: utf-8-unix -*-
"use strict";

console.log(Math.PI); //3.141592653589793
console.log(Math.SQRT2); //1.4142135623730951
console.log(Math.sqrt(3)); //1.7320508075688772

console.log(Math.abs(-3)); //3

console.log(Math.ceil(10.5)); //11
console.log(Math.floor(10.5)); //10
console.log(Math.round(10.5)); //11

console.log(Math.max(3,9,1,7,5)); //9
console.log(Math.min(3,9,1,7,5)); //1

console.log(Math.random()); //0.02861418432950935
console.log(Math.pow(2,8)); //256

let nums = [3,9,1,7,5];
console.log(Math.min.apply(null, nums));  //1
console.log(Math.max.apply(null, nums));  //9
