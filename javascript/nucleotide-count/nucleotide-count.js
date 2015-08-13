function dna (sequence) {
  if (!sequence) {
    sequence = '';
  }
  if (sequence.match(/[^AGCT]/)) {
    throw new Error("Only 'A', 'G', 'C', and 'T' nucleotides allowed, " +
                    "but " + match[0] + " was given");
  }

  var histogram_obj = sequence.split('').reduce(function (hist, nucleo) {
    hist[nucleo] += 1;
    return hist;
  }, { 'A': 0, 'G': 0, 'C': 0, 'T': 0 });

  function count (nucleoToCount) { return histogram_obj[nucleoToCount]; }

  function histogram () { return histogram_obj; }

  return { count: count, histogram: histogram };
}

module.exports = dna;
