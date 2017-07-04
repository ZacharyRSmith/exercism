"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
var isDivisibleBy = function isDivisibleBy(a, b) {
  return a % b === 0;
};

exports["default"] = function (year) {
  // if the year is not divisible by 4
  // if (year % 4) {
  //     return false;
  // }

  // if the year is not divisible by 100
  if (year % 100) {
    return !(year % 4);
  }

  return !(year % 400);

  if (year % 400) {
    // isDivBy 4 && 100
    return false;
  }
  return true;
  // if(isDivisibleBy(year, 100)) return isDivisibleBy(year, 400);
  // else return isDivisibleBy(year, 4);
};

module.exports = exports["default"];