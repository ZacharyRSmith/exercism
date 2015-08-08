function Beer () {}

Beer.prototype = {
  constructor: Beer,

  sing: function (start, end) {
    if (typeof end === 'undefined') { end = 0; }
    var song = "";

    for (var verse = start; verse >= end; verse--) {
      song += this.verse(verse);

      if (verse !== end) {
        song += "\n";
      }
    }

    return song;
  },

  verse: function (num) {
    if (num === 0) {
      return "No more bottles of beer on the wall, no more bottles of beer.\n" +
          "Go to the store and buy some more, 99 bottles of beer on the wall.\n";
    }
    if (num === 1) {
      return "1 bottle of beer on the wall, 1 bottle of beer.\n" +
          "Take it down and pass it around, no more bottles of beer on the wall.\n";
    }

    return num + " bottles of beer on the wall, " + num + " bottles of beer.\n" +
        "Take one down and pass it around, " + (num - 1) + " bottles of beer on the wall.\n";
  }
}

module.exports = new Beer();
