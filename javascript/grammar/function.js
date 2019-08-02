// -*- coding: utf-8-unix -*-
"use strict";

// argument, default argument
function sayThanks(name='xxx') {
  console.log(`Thank you for your purchase ${name}. We appreciate your business.`);
  
}
sayThanks('Cole');
sayThanks();

// Return
function monitorCount(rows, columns) {
  return rows * columns;
}
const numOfMonitors = monitorCount(5, 4);
console.log(numOfMonitors);

// Function Expressions
const plantNeedsWater = function plantNeedsWater(day) {
  if (day === 'Wednesday') {
    return true;
  } else {
    return false;
  }
};
console.log(plantNeedsWater('Tuesday'));

// Arrow Functions
const plantNeedsWater2 = (day) => {
  if (day === 'Wednesday') {
    return true;
  } else {
    return false;
  }
};
console.log(plantNeedsWater2('Tuesday'));

// Concise Body Arrow Functions 
const plantNeedsWater3 = day => day === 'Wednesday' ? true : false;
console.log(plantNeedsWater3('Tuesday'));
