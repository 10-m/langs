// -*- coding: utf-8-unix -*-
"use strict";

// For Loop
for (let count = 5; count <= 10; count++) {
  console.log(count);
}

// Reverse
for (let counter = 3; counter >= 0; counter--) {
  console.log(counter);
}

// Array
const vacationSpots = ['Bali', 'Paris', 'Tulum'];
for (let i = 0; i < vacationSpots.length; i++) {
  console.log('I would love to visit ' + vacationSpots[i]);
}

// Nested Loops
let bobsFollowers  = ['a', 'b', 'c', 'd'];
let tinasFollowers = ['a', 'b', 'A'];
let mutualFollowers = [];
for (let i = 0; i < bobsFollowers.length; i++) {
  for (let j = 0; j < tinasFollowers.length; j++) {
    if (bobsFollowers[i] === tinasFollowers[j]) {
      mutualFollowers.push(bobsFollowers[i]);
    }
  }  
}
console.log(mutualFollowers);

// While
const cards = ['diamond', 'spade', 'heart', 'club'];
let currentCard;
while (currentCard != 'spade') {
  currentCard = cards[Math.floor(Math.random() * 4)];
  console.log(currentCard);
}

// Do...While
let cupsOfSugarNeeded = 3;
let cupsAdded = 0;
do {
  cupsAdded++;
} while(cupsOfSugarNeeded > cupsAdded);

// break
const rapperArray = ["Lil' Kim", "Jay-Z", "Notorious B.I.G.", "Tupac"];
for (let i = 0; i < rapperArray.length; i++) {
  console.log(rapperArray[i]);
  console.log("And if you don't know, now you know.");
  if (rapperArray[i] === 'Notorious B.I.G.') {
    break;
  }
}

