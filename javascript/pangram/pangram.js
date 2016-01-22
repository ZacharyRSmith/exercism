var Pangram = function (input) {
  // is neither an object nor literal string
  if (!input.valueOf || typeof input.valueOf() !== 'string') return;

  // This converts a String object into a primitive string
  this._input = input.valueOf();
};
Pangram.prototype.isPangram = function () {
  if (this._input === undefined) return;

  // do not stop searching input if reached end of a sentence
  // do not worry about returning true early...iterate through entire input

  // hash table of all greek letters
  var foundLetters = {
    'a': false,
    'b': false,
    'c': false,
    'd': false,
    'e': false,
    'f': false,
    'g': false,
    'h': false,
    'i': false,
    'j': false,
    'k': false,
    'l': false,
    'm': false,
    'n': false,
    'o': false,
    'p': false,
    'q': false,
    'r': false,
    's': false,
    't': false,
    'u': false,
    'v': false,
    'w': false,
    'x': false,
    'y': false,
    'z': false
  };

  // iterate through input, marking true in hash table
  this._input.split('').forEach(function (char) {
    char = char.toLowerCase(); // search for pangram case insensitively

    if (foundLetters.hasOwnProperty(char)) {
      foundLetters[char] = true;
    }
  });

  return Object.keys(foundLetters).every(function (letter) {
    return foundLetters[letter];
  });
};


module.exports = Pangram;
