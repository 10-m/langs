// -*- coding: utf-8-unix -*-
"use strict";

// Blocks and Scope
const city = 'New York City';

function logCitySkyline() {
  let skyscraper = 'Empire State Building';
  return 'The stars over the ' + skyscraper + ' in ' + city;
}
console.log(logCitySkyline());

// Global Scope
const satellite = 'The Moon';
const galaxy = 'The Milky Way';
const stars = 'North Star';
function callMyNightSky() {
  return 'Night Sky: ' + satellite + ', ' + stars + ', and ' + galaxy;
}
console.log(callMyNightSky());

// Block Scope
function logVisibleLightWaves() {
  const lightWaves = 'Moonlight';
  console.log(lightWaves);
}
logVisibleLightWaves();
try {
  console.log(lightWaves);
}
catch (e) {
  console.log(e);
}

// Scope Pollution
const satellite2 = 'The Moon';
const galaxy2 = 'The Milky Way';
let stars2 = 'North Star';

const callMyNightSky2 = () => {
  stars2 = 'Sirius';
	return 'Night Sky: ' + satellite2 + ', ' + stars2 + ', ' + galaxy2;
};
console.log(callMyNightSky2());
console.log(stars2);

// Practice Good Scoping
const logVisibleLightWaves2 = () => {
  let lightWaves = 'Moonligcht';
	let region = 'The Arctic';
  // Add if statement here:
  if (region === 'The Arctic') {
    let lightWaves = 'Northern Lights';
    console.log(lightWaves);
  }
  console.log(lightWaves);
};
logVisibleLightWaves2();
