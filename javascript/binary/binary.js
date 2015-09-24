var Binary = function (str) {
  this.toDecimal = function () {
    if (/[^0-1]+/.test(str)) {
      return 0;
    }
    var byPowersOfTwo = str.split('').reverse();

    return byPowersOfTwo.reduce(function (decimal, crnt, i) {
      return decimal + parseInt(crnt) * Math.pow(2, i);
    }, 0);
  };
};

module.exports = Binary;
