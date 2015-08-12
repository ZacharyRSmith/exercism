function dna (sequence) {
  return new Acid(sequence);
}


function Acid (sequence) {
  this.sequence = this.validateSequence(sequence);
}

Acid.prototype = {
  constructor: Acid,

  count: function (nucToCount) {
    var regex = new RegExp(nucToCount, 'g');
    var matches = this.sequence.match(regex);

    if (!matches) { return 0; }

    return matches.length;
  },

  histogram: function () {
    return {
      A: this.count('A'),
      T: this.count('T'),
      C: this.count('C'),
      G: this.count('G'),
    };
  },

  validateSequence: function (sequence) {
    if (!sequence) { return ''; }

    var match = sequence.match(/[^AGCT]/);

    if (match) {
        throw new Error("Only 'A', 'G', 'C', and 'T' nucleotides allowed, " +
                        "but " + match[0] + "was given");
    }

    return sequence;
  }
};

module.exports = dna;
