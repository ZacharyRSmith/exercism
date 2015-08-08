const INVALID_NUMBER = "0000000000";

function PhoneNumber (input) {
  this.num = this.validateInput(input);
}

PhoneNumber.prototype = {
  constructor: PhoneNumber,

  areaCode: function () {
    if (this.num === INVALID_NUMBER) { return INVALID_NUMBER; }

    return this.num.substr(0,3);
  },

  number: function () { return this.num; },

  toString: function () {
    if (this.num === INVALID_NUMBER) { return INVALID_NUMBER; }

    return this.num.replace(/^(\d{3})(\d{3})(\d{4})/, "($1) $2-$3");
  },

  validateInput: function (input) {
    var digits = input.replace(/\D/g, '');

    if (digits.length < 10) { return INVALID_NUMBER; }
    if (digits.length === 11) {
      if (digits[0] == 1) { digits = digits.substr(1); }
      else { return INVALID_NUMBER; }
    }
    if (digits.length > 11) { return INVALID_NUMBER; }

    return digits;
  }
}

module.exports = PhoneNumber;
