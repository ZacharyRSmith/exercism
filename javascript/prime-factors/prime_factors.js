module.exports = {
  for: function (int) {
    var i = 2;
    var result = [];

    while (int > 1) {
      if (int % i === 0) {
        int /= i;
        result.push(i);
      } else {
        i += 1;
      }
    }

    return result;
  }
};
