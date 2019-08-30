// -*- coding: utf-8-unix -*-
"use strict";

// this Keyword
const robot = {
  model: '1E78V2',
  energyLevel: 100,
  provideInfo() {
    return(`I am ${this.model} and my current energy level is ${this.energyLevel}.`);
  }
};
console.log(robot.provideInfo());

// Arrow Functions and this
const robot2 = {
  energyLevel: 100,
  checkEnergy() {
    console.log(`Energy is currently at ${this.energyLevel}%.`);
  }
};
robot2.checkEnergy();

// Privacy
const robot3 = {
  _energyLevel: 100,
  recharge(){
    this._energyLevel += 30;
    console.log(`Recharged! Energy is currently at ${this._energyLevel}%.`);
  }
};

robot3._energyLevel = 'high';
robot3.recharge();

// Getters
const robot4 = {
  _model: '1E78V2',
  _energyLevel: 100,
  get energyLevel() {
    if (typeof(this._energyLevel) === 'number') {
      return(`My current energy level is ${this._energyLevel}`);
    }
    else {
      return('System malfunction: cannot retrieve energy level');
    }
  }
};
console.log(robot4.energyLevel);

// Setters
const robot5 = {
  _model: '1E78V2',
  _energyLevel: 100,
  _numOfSensors: 15,
  get numOfSensors(){
    if (typeof this._numOfSensors === 'number'){
      return this._numOfSensors;
    }
    else {
      return 'Sensors are currently down.';
    }
  },
  set numOfSensors(num) {
    if ((typeof(num) === 'number') && (num >= 0)) {
      this._numOfSensors = num;
    }
    else {
      console.log('Pass in a number that is greater than or equal to 0');
    }
  }
};

robot5.numOfSensors = 100;
console.log(robot5.numOfSensors);

// Factory Functions
const robotFactory = (model, mobile) => {
  return {
    model: model,
    mobile: mobile,
    beep() {
      console.log('Beep Boop');
    }
  };
};
const tinCan = robotFactory('P-500', true);
tinCan.beep();

// Property Value Shorthand
const robotFactory2 = (model, mobile) => {
  return {
    model,
    mobile,
    beep() {
      console.log('Beep Boop');
    }
  };
};
const newRobot = robotFactory2('P-501', false);
console.log(newRobot.model);
console.log(newRobot.mobile);

// Destructured Assignment
const robot6 = {
  model: '1E78V2',
  energyLevel: 100,
  functionality: {
    beep() {
      console.log('Beep Boop');
    },
    fireLaser() {
      console.log('Pew Pew');
    },
  }
};
const {functionality} = robot6;
functionality.beep();

// Built-in Object Methods
const robot7 = {
  model: 'SAL-1000',
  mobile: true,
  sentient: false,
  armor: 'Steel-plated',
  energyLevel: 75
};

// What is missing in the following method call?
const robotKeys = Object.keys(robot7);
console.log(robotKeys);

// Declare newRobot below this line:
const newRobot2 = {laserBlaster: true, voiceRecognition: true};
Object.assign(newRobot2, robot7);
console.log(newRobot2);
