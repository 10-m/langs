// -*- coding: utf-8-unix -*-
"use strict";
try {
  throw Error('This error will get caught');
} catch (e) {
  console.log(e);
}

function capAllElements(arr){
  try {
	  arr.forEach((el, index, array) => {
      array[index] = el.toUpperCase();
    });
  } catch(e) {
    console.log(e);
  }
}

capAllElements('Incorrect argument');
