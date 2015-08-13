function School() {
  'use strict';

  var db = {};

  function _deepCopy(arg) {
    if (arg instanceof Object) {
      var copy = Object.create(Object.getPrototypeOf(arg));

      Object.keys(arg).forEach(function (key) {
        copy[key] = _deepCopy(arg[key]);
      });

      return copy;
    }
    else { return arg; }
  }

  function add(student, grade) {
    db[grade] = db[grade] || [];
    db[grade].push(student);
    db[grade].sort();
  }

  function grade(number) {
    return _deepCopy(db[number] || []);
  }

  function roster() {
    return _deepCopy(db);
  }

  return { add: add, grade: grade, roster: roster };
}

module.exports = School;
