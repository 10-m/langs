// -*- coding: utf-8-unix -*-
"use strict";

// Dateオブジェクト生成
console.log(new Date()); //実行時の日時
console.log(new Date(2017, 8, 6, 9, 48, 15)); //Wed Sep 06 09:48:15 GMT+09:00 2017
console.log(new Date('2017/09/06 09:48:15')); //Wed Sep 06 09:48:15 GMT+09:00 2017
console.log(new Date(1504658899068)); //Wed Sep 06 09:48:19 GMT+09:00 2017

// Dateオブジェクトのメンバー
let d = new Date(2017, 8, 6, 9, 48, 15, 777);

console.log(d.getFullYear()); //2017
console.log(d.getMonth()); //8(=9月)
console.log(d.getDate()); //6
console.log(d.getDay()); //3(=水曜日)
console.log(d.getHours()); //9
console.log(d.getMinutes()); //48
console.log(d.getSeconds()); //15
console.log(d.getMilliseconds()); //777
console.log(d.getTime()); //1.504658895777E12

console.log(d.getTimezoneOffset()); //-540

// セット
d.setFullYear(2020);
d.setMonth(0);
d.setDate(1);
d.setHours(1);
d.setMinutes(11);
d.setSeconds(11);
d.setMilliseconds(111);

// メソッド
console.log(d.toString()); //Wed Jan 01 2020 01:11:11 GMT+0900 (JST)
console.log(d.toDateString()); //Wed Jan 01 2020
console.log(d.toTimeString()); //01:11:11 GMT+0900 (JST)
console.log(d.toJSON()); //01:11:11 GMT+0900 (JST)
