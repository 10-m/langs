// -*- coding: utf-8-unix -*-
"use strict";

let array = ['Bob', 'Tom', 'Jay', 'Tom'];

console.log(array.length); //4

console.log(array.toString()); //Bob,Tom,Jay,Tom
console.log(array.join('|')); //Bob|Tom|Jay|Tom

console.log(array.concat(['Dan'])); //[Bob, Tom, Jay, Tom, Dan]
console.log(array.slice(1, 3)); //[Tom, Jay]

console.log(array.indexOf('Tom')); //1
console.log(array.lastIndexOf('Tom')); //3

let element = 'Tom';
if(array.indexOf(element) !== -1) {
  console.log('%sが含まれています', element);
} else {
  console.log('%sは含まれていません', element);
}

// オブジェクト変更
{
  let array = ['Bob', 'Tom', 'Jay', 'Tom'];

  array.push('Dan');
  console.log(array); //[Bob, Tom, Jay, Tom, Dan]

  array.unshift('Ivy');
  console.log(array); //[Ivy, Bob, Tom, Jay, Tom, Dan]

  array.reverse();
  console.log(array); //[Dan, Tom, Jay, Tom, Bob, Ivy]

  array.sort();
  console.log(array); //[Bob, Dan, Ivy, Jay, Tom, Tom]

  console.log(array.pop()); //Tom
  console.log(array); //[Bob, Dan, Ivy, Jay, Tom]

  console.log(array.shift()); //Bob
  console.log(array); //[Dan, Ivy, Jay, Tom]

  console.log(array.splice(2,2,'Kim')); //[Jay, Tom]
  console.log(array); //[Dan, Ivy, Kim]
}

// 置換・削除・追加
{
  let array = ['Bob', 'Tom', 'Jay', 'Dan', 'Ivy'];

  // 置換
  array.splice(1,2,'Kim');
  console.log(array); //[Bob, Kim, Dan, Ivy]

  // 削除
  array.splice(1,2);
  console.log(array); //[Bob, Ivy]

  // 追加
  array.splice(1, 0, 'Leo');
  console.log(array); //[Bob, Leo, Ivy]
}

// forEach
{
  let array1 = ['Bob', 'Tom', 'Jay', 'Dan'];

  array1.forEach((name, index, array) => {
    console.log('%s:Hello %s !', index, name);
  });
}

// その他メソッド
{
  let array1 = ['Bob', 'Tom', 'Jay', 'Dan'];

  let isThreeChar = array1.every(function(name, index, array) {
    return (name.length === 3);
  });
  console.log(isThreeChar); //true

  let hasBob = array1.some(function(name, index, array) {
    return (name === 'Bob');
  });
  console.log(hasBob); //true

  let array2 = array1.filter(function(name, index, array) {
    return (name.charAt(1) === 'o');
  });
  console.log(array2); //[Bob, Tom]

  let array3 = array1.map(function(name, index, array) {
    return name.length;
  });
  console.log(array3); //[3, 3, 3, 3]
}

// reduce
{
  let array1 = ['Bob', 'Tom', 'Jay', 'Dan'];

  let result1 = array1.reduce(function(str, name, index, array) {
    return str + name;
  });
  console.log(result1); //BobTomJayDan

  let result2 = array1.reduceRight(function(str, name, index, array) {
    return str + name;
  });
  console.log(result2); //DanJayTomBob
}
