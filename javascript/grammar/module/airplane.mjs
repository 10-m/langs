// -*- coding: utf-8-unix -*-
"use strict";

// export default
export let availableAirplanes = [
  {
    name: 'AeroJet', 
    maxSpeed: 1200,
    minSpeed: 300,
    fuelCapacity: 800, 
    availableStaff: ['pilots',
                     'flightAttendants', 
                     'engineers', 
                     'medicalAssistance', 
                     'sensorOperators']
  },
  {
    name: 'SkyJet', 
    maxSpeed: 800,
    minSpeed: 200,
    elCapacity: 500,
    availableStaff: ['pilots', 'flightAttendants']
  }];

export let flightRequirements = {
  requiredStaff: 4,
  requiredSpeedRange: 700,
};

export function meetsStaffRequirements(availableStaff, requiredStaff) {
  if (availableStaff.length >= requiredStaff) {
    return true;
  }
  else {
    return false;
  }
}

export function meetsSpeedRangeRequirements(maxSpeed, minSpeed, requiredSpeedRange) {
  let range = maxSpeed - minSpeed;
  if (range > requiredSpeedRange) {
    return true;
  }
  else {
    return false;
  }
}

export default meetsSpeedRangeRequirements;
