function anagram (input) {
  var origWord = input.trim().toLowerCase();


  var isMatch = function (candidate) {
    candidate = candidate.toLowerCase();

    if (candidate === origWord) { return false; }

    return candidate.split('').sort().join('') ===
           origWord.split('').sort().join('');
  };


  var matches = function (arg) {
    var candidates = [];
    // Iterate over arguments instead of slice for optimization:
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments
    if (arg instanceof Array) {
      candidates = arg;
    }
    else {
      for (var key in arguments) {
        candidates.push(arguments[key]);
      }
    }

    return candidates.filter(function (candidate) {
      return isMatch(candidate.toLowerCase());
    }, this);
  };

  return { matches: matches };
}

module.exports = anagram;
