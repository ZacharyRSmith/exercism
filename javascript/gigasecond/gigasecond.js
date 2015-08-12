module.exports = function (expulsionDay) {
  'use strict';

  var GIGASECOND = Math.pow(10, 9);

  this.date = function () {
    var happyDay = expulsionDay;
    happyDay.setSeconds(happyDay.getSeconds() + GIGASECOND);
    happyDay.setHours(0, 0, 0, 0);

    return happyDay;
  };
};
