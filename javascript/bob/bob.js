//
// This is only a SKELETON file for the "Bob" exercise. It's been provided as a
// convenience to get you started writing code faster.
//

var Bob = function() {};

Bob.prototype.hey = function(input) {
  // No input:
  if (!input.trim()) { return 'Fine. Be that way!'; }

  // Yelling:
  if (input.toUpperCase() === input && /[a-z]/i.test(input)) {
    return 'Whoa, chill out!';
  }

  // Questions:
  if (input.substr(input.length - 1) === '?') {
    return 'Sure.';
  }

  return 'Whatever.';
};

module.exports = Bob;
