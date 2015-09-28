module.exports = {
  discard: function(ary, test) {
    return ary.reduce(function(result, elt) {
      if (!test(elt)) {
        result.push(elt);
      }
      return result;
    }, []);
  },

  keep: function(ary, test) {
    return ary.reduce(function(result, elt) {
      if (test(elt)) {
        result.push(elt);
      }
      return result;
    }, []);
  }
};
