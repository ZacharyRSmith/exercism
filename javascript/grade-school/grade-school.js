function School () {
  var db = {};

  this.add = function (name, grade) {
    if (!db[grade]) { db[grade] = []; }

    db[grade].push(name);
    db[grade].sort();
  };

  this.grade = function (grade) {
    if (!db[grade]) { return []; }

    return db[grade];
  };

  this.roster = function () { return db; };
}

module.exports = School;
