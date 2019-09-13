// -*- coding: utf-8-unix -*-
"use strict";

let sayHello = new Function('name', "console.log('Hello %s !', name)");
sayHello('Bob');

let Person = function(name, age){
  this.name = name;
  this.age = age;
};
console.log(Person.length);
console.log(Person.toString());

// call method
let Person2 = function(name){
  this.name = name;
};

Person2.prototype.hello = function() {
  return "Hello! I'm " + this.name + ".";
};

let Dog = function(name) {
  this.name = name;
}

let person2 = new Person2('Bob');
let dog1 = new Dog('Pochi');
console.log(person2.hello.call(dog1)); //Hello! I'm Pochi.
console.log(Person2.prototype.hello.call(dog1)); //Hello! I'm Pochi.

// apply
// 2 dim to 1 dim
let array = [[10],[20],[30],[40],[50]];
console.log(Array.prototype.concat.apply([],array)); //[10, 20, 30, 40, 50]
console.log([].concat([10],[20],[30],[40],[50]));  //[10, 20, 30, 40, 50]
