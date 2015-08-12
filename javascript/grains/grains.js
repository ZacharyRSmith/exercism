function Grains () {}

Grains.prototype = {
    constructor: Grains,

    square: function (n) { return Math.pow(2, n-1); },

    // The sum of squares is the square of the next int minus 1.
    total: function () { return this.square(65) - 1; }
};

module.exports = Grains;
