var SECONDS_PER_EARTH_YR = 31557600;

function SpaceAge (seconds) {
  this._seconds = seconds;
}

SpaceAge.prototype = {
  constructor: SpaceAge,

  convertYears: function (inEarthYrs) {
    return +((this.seconds / SECONDS_PER_EARTH_YR) / inEarthYrs).toFixed(2);
  },

  get seconds() { return this._seconds; },

  onEarth: function () {
    return this.convertYears(1);
  },

  onMercury: function () {
    return this.convertYears(0.2408467);
  },

  onVenus: function () {
    return this.convertYears(0.61519726);
  },

  onMars: function () {
    return this.convertYears(1.8808158);
  },

  onJupiter: function () {
    return this.convertYears(11.862615);
  },

  onSaturn: function () {
    return this.convertYears(29.447498);
  },

  onUranus: function () {
    return this.convertYears(84.016846);
  },

  onNeptune: function () {
    return this.convertYears(164.79132);
  }
};

module.exports = SpaceAge;
