function anagram (subject) {
  return new AnagramMatcher(subject);
}

function AnagramMatcher (subject) {
  this.subject = subject.toLowerCase();

  this.isMatch = function (candidate) {
    if (candidate.length !== this.subject.length) { return false; }
    if (candidate === this.subject) { return false; }
    var left_of_subject = this.subject;

    for (var char in candidate) {
      var charInd = left_of_subject.indexOf(candidate[char]);

      if (charInd === -1) { return false; }

      left_of_subject = this.removeChar(candidate[char], left_of_subject);
    }

    return true;
  };

  this.removeChar = function (char, str) {
    var charInd = str.indexOf(char);

    return str.slice(0, charInd) + str.slice(charInd + 1);
  };

  this.matches = function () {
    var input = [];
    // Iterate over arguments instead of slice for optimization:
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments
    for (var arg in arguments) { input.push(arguments[arg]); }

    var matches = [];
    var self = this;

    input.forEach(function (arg) {
      if (arg instanceof Array) {
        arg.forEach(function (word) {
          if (self.isMatch(word.toLowerCase())) { matches.push(word); }
        });
      } else {
        if (self.isMatch(arg.toLowerCase())) { matches.push(arg); }
      }
    });

    return matches;
  };
}

module.exports = anagram;
