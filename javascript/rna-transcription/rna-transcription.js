module.exports = function (dna) {
  if (!dna || /[^ATCG]/.test(dna)) {
    throw new Error("shenanigans!!");
  }

  return dna.replace(/\w/g, function (match) {
    switch (match) {
      case 'C': return 'G';
      case 'G': return 'C';
      case 'A': return 'U';
      case 'T': return 'A';
    }
  });
};
