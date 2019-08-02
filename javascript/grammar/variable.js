// --- variables
// let
let meal = 'Enchiladas';
console.log(meal); // Output: Enchiladas
meal = 'Burrito';
console.log(meal); // Output: Burrito

// const
const entree = 'Enchiladas';
console.log(entree);
try {
  entree = 'Tacos';
}
catch (e) {
  console.log(e);
}

// Mathematical Assignment Operators
let levelUp = 10;
let powerLevel = 9001;
let multiplyMe = 32;
let quarterMe = 1152;

levelUp += 5;
powerLevel -= 100;
multiplyMe *= 11;
quarterMe /= 4;

console.log('The value of levelUp:', levelUp); 
console.log('The value of powerLevel:', powerLevel); 
console.log('The value of multiplyMe:', multiplyMe); 
console.log('The value of quarterMe:', quarterMe);

// The Increment and Decrement Operator
let gainedDollar = 3;
let lostDollar = 50;

gainedDollar++;
lostDollar--;

console.log(gainedDollar);
console.log(lostDollar);

// String Concatenation with Variables
let favoriteAnimal = 'dog';
console.log('My favorite animal: ' + favoriteAnimal);

// String Interpolation
let myName = 'xxx';
let myCity = 'yyy';
console.log(`My name is ${myName}. My favorite city is ${myCity}.`);

// typeof operator
let newVariable = 'Playing around with typeof.';
console.log(typeof newVariable);
newVariable = 1;
console.log(typeof newVariable);
