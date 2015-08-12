var SECONDS_PER_EARTH_YR = 31557600;

function SpaceAge (seconds) {
  return {
    seconds: seconds,
    onEarth: this.convertYears(1),
    onMercury: this.convertYears(0.2408467),
    onVenus: this.convertYears(0.61519726),
    onMars: this.convertYears(1.8808158),
    onJupiter: this.convertYears(11.862615),
    onSaturn: this.convertYears(29.447498),
    onUranus: this.convertYears(84.016846),
    onNeptune: this.convertYears(164.79132)
  };
}

SpaceAge.prototype = {
  constructor: SpaceAge,

  convertYears: function (inEarthYrs) {
    return function () {
      return +((this.seconds / SECONDS_PER_EARTH_YR) /
               inEarthYrs).toFixed(2);
    };
  },
};

module.exports = SpaceAge;
