function Song () {
  this.verse8 = "I know an old lady who swallowed a horse.\n" +
                "She's dead, of course!\n";
}

Song.prototype = {
  constructor: Song,

  getFirstLine: function (animal) {
    return "I know an old lady who swallowed a " + animal + ".\n";
  },

  getRepeatedLines: function (verseNum) {
    var repeatedLines = "";

    switch(verseNum) {
      case 7:
        repeatedLines += "She swallowed the cow to catch the goat.\n";
      case 6:
        repeatedLines += "She swallowed the goat to catch the dog.\n";
      case 5:
        repeatedLines += "She swallowed the dog to catch the cat.\n";
      case 4:
        repeatedLines += "She swallowed the cat to catch the bird.\n";
      case 3:
        repeatedLines += "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.\n";
      case 2:
        repeatedLines += "She swallowed the spider to catch the fly.\n";
      case 1:
        repeatedLines += "I don't know why she swallowed the fly. Perhaps she'll die.\n";
    }

    return repeatedLines;
  },

  getUniqueLines: function (verseNum) {
    var uniqueLines = "";

    switch(verseNum) {
      case 1:
        uniqueLines += this.getFirstLine('fly');
        break;
      case 2:
        uniqueLines += this.getFirstLine('spider');
        uniqueLines += "It wriggled and jiggled and tickled inside her.\n";
        break;
      case 3:
        uniqueLines += this.getFirstLine('bird');
        uniqueLines += "How absurd to swallow a bird!\n";
        break;
      case 4:
        uniqueLines += this.getFirstLine('cat');
        uniqueLines += "Imagine that, to swallow a cat!\n";
        break;
      case 5:
        uniqueLines += this.getFirstLine('dog');
        uniqueLines += "What a hog, to swallow a dog!\n";
        break;
      case 6:
        uniqueLines += this.getFirstLine('goat');
        uniqueLines += "Just opened her throat and swallowed a goat!\n";
        break;
      case 7:
        uniqueLines += this.getFirstLine('cow');
        uniqueLines += "I don't know how she swallowed a cow!\n";
        break;
    }

    return uniqueLines;
  },

  verse: function (verseNum) {
    if (verseNum === 8) { return this.verse8; }
    var verse = "";

    verse += this.getUniqueLines(verseNum);
    verse += this.getRepeatedLines(verseNum);

    return verse;
  },

  verses: function (verseStart, verseEnd) {
    var verses = "";

    for (var num = verseStart; num <= verseEnd; num++) {
      verses += this.verse(num);
      verses += "\n";
    }

    return verses;
  }
}

module.exports = new Song();
