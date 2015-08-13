function randomLetter () {
  var letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

  return letters.charAt(Math.floor(Math.random() * letters.length));
}


function Robot() {
  'use strict';

  this._name = null;
  this.name = this.genName();
}

Robot.usedNames = {};

Robot.prototype = {
  constructor: Robot,

  genName: function () {
    // This awesome err msg will never see the light of day. ;_; Checking the
    // length was slowing the program down too much
    //
//     if (Object.keys(this.constructor.usedNames).length >= 676000) {
//       throw new Error("All possible names have been taken. " +
//                           "Our robots are taking over the world!");
//     }

    var name = randomLetter().toUpperCase();
    name += randomLetter().toUpperCase();
    name += (Math.random() + '').substr(2, 3);

    if (name in this.constructor.usedNames) {
      return this.genName();
    }

    return name;
  },

  get name () { return this._name; },

  set name (newName) {
    if (!(/^[A-Z]{2}\d{3}$/).test(newName)) {
      throw new Error("Name must be 2 capital letters followed by 3 ints.");
    }
    if (newName in this.constructor.usedNames) {
      throw new Error("Name " + newName + " has already been used!");
    }

    this.constructor.usedNames[newName] = true;
    this._name = newName;
  },

  reset: function() { this.name = this.genName(); },
};

module.exports = Robot;
