function School () {
  var db = {};

  this.add = function (name, grade) {
    db[grade] = (db[grade] || []);

    db[grade].push(name);
    db[grade].sort();
  };

  this.grade = function (grade) {
    if (!db[grade]) { return []; }

    return db[grade];
  };

  this.roster = function () {
      var dup = db;
      return dup;
  };
}


// function School() {
//   var rosterDb = {};

//   this.roster = function() {
//     var dup = {},
//         k;
//     for (k in rosterDb) {
//       dup[k] = rosterDb[k];
//     }
//     return dup;
//   };

//   this.add = function(name, grade) {
//     rosterDb[grade] = rosterDb[grade] || [];
//     rosterDb[grade].push(name);
//     rosterDb[grade].sort();
//   };

//   this.grade = function(n) {
//     return (rosterDb[n] ? rosterDb[n] : []);
//   };
// }

// module.exports = School;