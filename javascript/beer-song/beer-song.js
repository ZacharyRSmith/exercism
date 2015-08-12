function Beer () {}

Beer.prototype = {
  constructor: Beer,

  sing: function (start, end) {
    end = (end || 0);
    var verses = [];

    for (var vNum = start; vNum >= end; vNum--) {
      verses.push(this.verse(vNum));
    }

    return verses.join('\n');
  },

  verse: function (n) {
    if (n === 0) {
      return "No more bottles of beer on the wall, no more bottles of beer.\n" +
          "Go to the store and buy some more, 99 bottles of beer on the wall.\n";
    }
    if (n === 1) {
      return "1 bottle of beer on the wall, 1 bottle of beer.\n" +
          "Take it down and pass it around, no more bottles of beer on the wall.\n";
    }

    return n + " bottles of beer on the wall, " + n + " bottles of beer.\n" +
        "Take one down and pass it around, " + (n - 1) +
        " bottle" + (n - 1 === 1 ? '' : 's') + " of beer on the wall.\n";
  }
};

module.exports = new Beer();
