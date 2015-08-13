function dna (sequence) {
  if (!sequence) {
    sequence = '';
  }
  if (sequence.match(/[^AGCT]/)) {
    throw new Error("Only 'A', 'G', 'C', and 'T' nucleotides allowed, " +
                    "but " + match[0] + " was given");
  }

  var histogram_obj = {
    'A': ((/A/).test(sequence) ? sequence.match(/A/g).length : 0),
    'G': ((/G/).test(sequence) ? sequence.match(/G/g).length : 0),
    'C': ((/C/).test(sequence) ? sequence.match(/C/g).length : 0),
    'T': ((/T/).test(sequence) ? sequence.match(/T/g).length : 0)
  }

  function count (nucleoToCount) { return histogram_obj[nucleoToCount]; }

  function histogram () { return histogram_obj; }

  return { count: count, histogram: histogram };
}

module.exports = dna;
