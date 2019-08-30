// -*- coding: utf-8-unix -*-
"use strict";

let str = "My name is Bob.";

console.log(str.length); //15
console.log(str.charAt(0)); //M
console.log(str.charCodeAt(0)); //77

console.log(str.slice(3,7)); //name
console.log(str.substring(3,7)); //name
console.log(str.substr(3,4)); //name

console.log(str.split(' ')); //[My, name, is, Bob.]

console.log(str.toLowerCase()); //my name is bob.
console.log(str.toUpperCase()); //MY NAME IS BOB.

str = str.concat(" My dog's name is also Bob.");
console.log(str); //My name is Bob. My dog's name is also Bob.

console.log(str.indexOf('Bob')); //11
console.log(str.lastIndexOf('Bob')); //38

console.log('Bob'.localeCompare('Abc')); //1
console.log('Bob'.localeCompare('Bob')); //0
console.log('Bob'.localeCompare('Cde')); //-1

console.log('   Bob   '.trim()); //Bob

{
  let str = 'My name is Bob.';
  let subStr = 'Bob';

  if(str.indexOf(subStr) !== -1) {
    console.log('%sが含まれています', subStr);
  } else {
    console.log('%sは含まれていません', subStr);
  }
}
