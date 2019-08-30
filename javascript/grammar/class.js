// -*- coding: utf-8-unix -*-
"use strict";

// Introduction 
class Dog {
  constructor(name) {
    this._name = name;
    this._behavior = 0;
  }

  get name() {
    return this._name;
  }
  get behavior() {
    return this._behavior;
  }   

  incrementBehavior() {
    this._behavior ++;
  }
}
const halley = new Dog('Halley');
console.log(halley.name); // Print name value to console
console.log(halley.behavior); // Print behavior value to console
halley.incrementBehavior(); // Add one to behavior
console.log(halley.name); // Print name value to console
console.log(halley.behavior); // Print behavior value to console

// Constructor
class Surgeon {
  constructor(name, department) {
    this.name = name;
    this.department = department;
  }
}

// Instance
const surgeonCurry = new Surgeon('Curry', 'Cardiovascular');
const surgeonDurant = new Surgeon('Durant', 'Orthopedics');

// Methods
class Surgeon2 {
  constructor(name, department) {
    this._name = name;
    this._department = department;
    this._remainingVacationDays = 20;
  }
  get name() {
    return this._name;
  }
  get department() {
    return this._department;
  }
  get remainingVacationDays() {
    return this._remainingVacationDays;
  }
  takeVacationDays(dayOff) {
    this._remainingVacationDays -= dayOff;
    return this._remainingVacationDays;
  }
}

const surgeonCurry2 = new Surgeon2('Curry', 'Cardiovascular');
const surgeonDurant2 = new Surgeon2('Durant', 'Orthopedics');

// Method Calls
console.log(surgeonCurry2.name);
console.log(surgeonCurry2.takeVacationDays(3));
console.log(surgeonCurry2.remainingVacationDays);

// Inheritance
class HospitalEmployee {
  constructor(name) {
    this._name = name;
    this._remainingVacationDays = 20;
  }
  
  get name() {
    return this._name;
  }
  
  get remainingVacationDays() {
    return this._remainingVacationDays;
  }
  
  takeVacationDays(daysOff) {
    this._remainingVacationDays -= daysOff;
  }

  static generatePassword() {
    return Math.round(Math.random() * 10000);
  }
}

class Nurse extends HospitalEmployee {
  constructor(name, certifications) {
    super(name);
    this._certifications = certifications;
  }

  get certifications() {
    return this._certifications;
  }

  addCertification(newCertification) {
    this._certifications.push(newCertification);
  }
}

const nurseOlynyk = new Nurse('Olynyk', ['Trauma', 'Pediatrics']);
nurseOlynyk.takeVacationDays(5);
console.log(nurseOlynyk.remainingVacationDays);
nurseOlynyk.addCertification ('Genetics');
console.log(nurseOlynyk.certifications);

// Static Methods
console.log(HospitalEmployee.generatePassword());
console.log(Nurse.generatePassword());
