// -*- coding: utf-8-unix -*-
"use strict";

let obj = [
  {"name" : "Bob", "favorite" : ["apple","curry","video game"]},
  {"name" : "Tom", "favorite" : ["orange","ramen","programming"]},
  {"name" : "Jay", "favorite" : ["grape","sushi","shogi"]}
];

// object to string
let str = JSON.stringify(obj);
console.log(str);

// string to object
let persons = JSON.parse(str);
console.log(persons[0].name); //Bob
console.log(persons[1].favorite[2]); //programming
console.log(persons[2]); //{name=Jay, favorite=[grape, sushi, shogi]}
