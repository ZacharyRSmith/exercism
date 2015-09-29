function accumulate(ary, fn) {
  return ary.reduce(function(prev, crnt) {
    prev.push(fn(crnt));
    return prev;
  }, []);
};

module.exports = accumulate;
