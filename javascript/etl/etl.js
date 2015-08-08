function transform (old) {
  var rslt = {};

  for (var score in old) {
    old[score].forEach(function (ltr) {
      rslt[ltr.toLowerCase()] = parseInt(score);
    });
  }

  return rslt;
}

module.exports = transform;
