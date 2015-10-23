var _ = require('../lib/underscore');

var Sieve = function (limit) {
  'use strict';
  this.primes = this._findPrimes(limit);
};
Sieve.prototype = {
  constructor: Sieve,

  _getMultiples: function (num, limit) {
    var multiples = [];

    while (true) {
      var factor = factor + 1 || 2;
      var multiple = num * factor;
      if (multiple > limit) {
        break;
      }
      multiples.push(multiple);
    }

    return multiples;
  },

  _findPrimes: function (limit) {
    return Array.apply(0, { length: limit + 1 })
      .reduce(function(primes, isMarked, number, marked) {
        // - take the next available unmarked number in your list (it is prime)
        if (number < 2 || isMarked) {
          return primes;
        } else {
          primes.push(number);
        }
        // - mark all the multiples of that number (they are not prime)
        this._getMultiples(number, limit).forEach(function (multiple) {
          marked[multiple] = true;
        });

        return primes;
      }.bind(this), []);
  }
};

module.exports = Sieve;
