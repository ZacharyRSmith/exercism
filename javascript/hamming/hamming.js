var Hamming = {};
Hamming.compute = function (a, b) {
  if (a.length !== b.length) {
    throw new Error("DNA strands must be of equal length.");
  }
  var distance = 0;

  for (var i=0; i<a.length; i++) {
    if (a[i] !== b[i]) { distance += 1; }
  }

  return distance;
};

module.exports = Hamming;