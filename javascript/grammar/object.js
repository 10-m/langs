// -*- coding: utf-8-unix -*-
"use strict";

// Creating Object
let fasterShip  = {'color':'silver',
                  'Fuel Type':'Turbo Fuel'};
console.log(fasterShip);

// Accessing Properties
let spaceship = {
  homePlanet: 'Earth',
  color: 'silver',
  'Fuel Type': 'Turbo Fuel',
  numCrew: 5,
  'Active Mission' : true,
  flightPath: ['Venus', 'Mars', 'Saturn']
};

let crewCount = spaceship.numCrew;
let planetArray = spaceship.flightPath;
console.log(crewCount);
console.log(planetArray);

// Bracket Notation
let isActive = spaceship['Active Mission'];
let propName =  'Active Mission';
console.log(isActive);
console.log(spaceship[propName]);

// Property Assignment
console.log(spaceship);
spaceship.color = 'glorious gold';
spaceship.numEngines = 2;
delete spaceship['Secret Mission'];
console.log(spaceship);

// Methods
let retreatMessage = 'We no longer wish to conquer your planet. It is full of dogs, which we do not care for.';

let alienShip = {
  retreat(){console.log(retreatMessage);},
  takeOff(){console.log('Spim... Borp... Glix... Blastoff!');}
};

alienShip.retreat();
alienShip.takeOff();

// Nested Objects
let spaceship2 = {
  passengers: null,
  telescope: {
    yearBuilt: 2018,
    model: "91031-XLT",
    focalLength: 2032 
  },
  crew: {
    captain: { 
      name: 'Sandra', 
      degree: 'Computer Engineering', 
      encourageTeam() { console.log('We got this!'); },
     'favorite foods': ['cookies', 'cakes', 'candy', 'spinach'] }
  },
  engine: {
    model: "Nimbus2000"
  },
  nanoelectronics: {
    computer: {
      terabytes: 100,
      monitors: "HD"
    },
    backup: {
      battery: "Lithium",
      terabytes: 50
    }
  }
}; 

let capFave = spaceship2.crew.captain['favorite foods'][0];
spaceship2.passengers = [spaceship2['telescope',  'crew', 'engine', 'nanoelectronics']];
let firstPassenger = spaceship2.passengers[0];

// Pass By Reference
let spaceship3 = {
  'Fuel Type' : 'Turbo Fuel',
  homePlanet : 'Earth'
};

const greenEnergy = (obj) => {
  obj['Fuel Type'] = 'avocado oil';
};

const remotelyDisable = (obj) => {
  obj.disabled = true;
  
};

greenEnergy(spaceship3);
remotelyDisable(spaceship3);
console.log(spaceship3);

// Looping Through Objects
let spaceship4 = {
    crew: {
    captain: { 
        name: 'Lily', 
        degree: 'Computer Engineering', 
        cheerTeam() { console.log('You got this!') } 
        },
    'chief officer': { 
        name: 'Dan', 
        degree: 'Aerospace Engineering', 
        agree() { console.log('I agree, captain!') } 
        },
    medic: { 
        name: 'Clementine', 
        degree: 'Physics', 
        announce() { console.log(`Jets on!`) } },
    translator: {
        name: 'Shauna', 
        degree: 'Conservation Science', 
        powerFuel() { console.log('The tank is full!') } 
        }
    }
}; 

// Write your code below
for (let crewMember in spaceship4.crew) {
  console.log(`${crewMember}: ${spaceship4.crew[crewMember].name}`);
}

for (let crewMember in spaceship4.crew) {
  console.log(`${spaceship4.crew[crewMember].name}: ${spaceship4.crew[crewMember].degree}`);
}
