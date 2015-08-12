module.exports = function (dna) {
  if (!dna || /[^ATCG]/.test(dna)) {
    throw new Error("shenanigans!! D:");
  }

  var complements = {G: 'C', C: 'G', A: 'U', T: 'A'};
  return dna.replace(/\w/g, function (dnaNucleo) {
    return complements[dnaNucleo];
  });
};
