'use strict';

module.exports = function (expulsionDay) {
    var GIGASECOND = Math.pow(10, 9);

    this.date = function () {
        var happyDay = expulsionDay;
        happyDay.setSeconds(happyDay.getSeconds() + GIGASECOND);
        happyDay.setHours(0, 0, 0, 0);

        return happyDay;
    };
};
