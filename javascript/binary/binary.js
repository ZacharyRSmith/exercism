var Binary = function (str) {
  this.toDecimal = function () {
    var decimal = 0;
    var byPowersOfTwo = str.split('').reverse();

    for (var i = 0; i < byPowersOfTwo.length; i++) {
      if (byPowersOfTwo[i] !== '0' && byPowersOfTwo[i] !== '1') {
        decimal = 0;
        return decimal;
      }
      decimal += byPowersOfTwo[i] * Math.pow(2, i);
    }

    return decimal;
  };
};

module.exports = Binary;
