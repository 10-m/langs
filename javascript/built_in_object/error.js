// -*- coding: utf-8-unix -*-
"use strict";

// error object
try {
  throw new Error('発生させた例外');
} catch(e) {
  console.log(e.message); //発生させた例外
  console.log(e.name); //Error
  console.log(e.fileName); //コード
  console.log(e.lineNumber); //3
  console.log(e.stack); //at コード:3 (myFunction)
  console.log(e.toString()); //Error: 発生させた例外
}

// stack trace
function myFunction1() {
  throw new Error('発生させた例外');
}

function myFunction2() {
  myFunction1();
}

function myFunction3() {
  try{
    myFunction2();
  } catch(e) {
    console.log(e.stack);
  }
}
myFunction3();
