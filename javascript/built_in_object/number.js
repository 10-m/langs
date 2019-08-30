// -*- coding: utf-8-unix -*-
"use strict";

let x = 1000 / 3;
console.log(x.toString()); //333.3333333333333
console.log(x.toExponential(4)); //3.3333e+2
console.log(x.toFixed(4)); //333.3333
console.log(x.toFixed()); //333
console.log(x.toPrecision(4)); //333.3
console.log(x.toPrecision(2)); //3.3e+2

console.log(Number.MAX_VALUE); //1.7976931348623157E308
console.log(Number.MIN_VALUE); //4.9E-324
console.log(Number.NaN); //NaN
console.log(Number.POSITIVE_INFINITY); //Infinity
console.log(Number.NEGATIVE_INFINITY); //-Infinity
