function dna (sequence) {
  return new Acid(sequence);
}

function Acid (sequence) {
  this.sequence = this.validateSequence(sequence);
}

Acid.prototype = {
  constructor: Acid,

  count: function (nucToCount) {
    if (this.sequence === '') { return 0; }

    var count = 0;
    var seqAry = this.sequence.split('');

    seqAry.forEach(function (nuc) {
      if (nuc === nucToCount) { count += 1; }
    });

    return count;
  },

  histogram: function () {
    var histogram = { A: 0, T: 0, C: 0, G: 0 };

    if (this.sequence === '') { return histogram; }

    var seqAry = this.sequence.split('');

    seqAry.forEach(function (elt) {
      histogram[elt] += 1;
    });

    return histogram;
  },

  validateSequence: function (sequence) {
    if (!sequence) { return ''; }

    var seqAry = sequence.split('');

    seqAry.forEach(function (elt) {
      if (['A', 'G', 'C', 'T'].indexOf(elt) === -1) {
        throw new Error("Only 'A', 'G', 'C', and 'T' nucleotides allowed, " +
                        "but " + elt + "was given");
      }
    });

    return sequence;
  }
}

module.exports = dna;
