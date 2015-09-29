var ALLERGENS = {
  1: "eggs",
  2: "peanuts",
  4: "shellfish",
  8: "strawberries",
  16: "tomatoes",
  32: "chocolate",
  64: "pollen",
  128: "cats"
};

var Allergies = function(score) {
  return {
    list: function() {
      return Object.keys(ALLERGENS).reduce(function(prev, curr) {
        return (curr & score ? prev.concat(ALLERGENS[curr]) : prev);
      }, []);
    },
    allergicTo: function(allergen) {
      return (this.list().indexOf(allergen) !== -1);
    }
  };
};

module.exports = Allergies;

// 'use strict';

// var allergenScores = {
//   eggs: 1,
//   peanuts: 2,
//   shellfish: 4,
//   strawberries: 8,
//   tomatoes: 16,
//   chocolate: 32,
//   pollen: 64,
//   cats: 128
// };

// function Allergies(score) {
//   var allergens = Object.keys(allergenScores).reduce(function(res, allergen) {
//     if (allergenScores[allergen] & score) {
//       res.push(allergen);
//     }
//     return res;
//   }, []);

//   return {
//     allergicTo: function(allergen) {
//       return allergens.indexOf(allergen) !== -1;
//     },

//     list: function() {
//       return allergens;
//     }
//   };
// }

// module.exports = Allergies;
