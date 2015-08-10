function randomLetter () {
  var letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

  return letters.charAt(Math.floor(Math.random() * letters.length))

//   return Math.random().toString(36).replace(/[^a-z]+/g, '')[0];
}

function Robot () {
  this._name = this.genId();
}

Robot.usedNames = {};

Robot.prototype = {
  constructor: Robot,

  get name () { return this._name; },

  reset: function () { this._name = this.genId(); },

  genId: function () {
    var name = randomLetter().toUpperCase() + randomLetter().toUpperCase();
    // Get string of 3 random ints:
    name += (Math.random() + '').substr(2, 3);

    if (this.constructor.usedNames[name]) {
      return this.genId();
    } else {
      this.constructor.usedNames[name] = true;
    }

    return name;
  }
}

module.exports = Robot;
