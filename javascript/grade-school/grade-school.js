function School() {
  'use strict';

  var db = {};

  function _deepCopy(arg) {
    if (arg instanceof Object) {
      var copy = Object.create(Object.getPrototypeOf(arg));
      var props = Object.getOwnPropertyNames(arg);

      props.forEach(function (prop) {
        copy[prop] = _deepCopy(arg[prop]);
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
