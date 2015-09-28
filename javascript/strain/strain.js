function filter(ary, test) {
  return ary.reduce(function(result, elt) {
    if (test(elt)) {
      result.push(elt);
    }
    return result;
  }, []);
}

module.exports = {
  discard: function(ary, test) {
    return filter(ary, function(elt) {
      return !test(elt);
    });
  },

  keep: function(ary, test) {
    return filter(ary, test);
  }
};
