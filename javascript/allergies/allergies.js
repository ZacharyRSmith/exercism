function Allergies(score) {
  var allergens = {
    eggs: 1,
    peanuts: 2,
    shellfish: 4,
    strawberries: 8,
    tomatoes: 16,
    chocolate: 32,
    pollen: 64,
    cats: 128
  };

  var allergies = Object.keys(allergens).reduce(function(result, allergen) {
    if (allergens[allergen] & score) {
      result.push(allergen);
    }
    return result;
  }, []);

  this.allergicTo = function(allergen) {
    return allergies.indexOf(allergen) !== -1;
  };

  this.list = function() {
    return allergies;
  };
}

module.exports = Allergies;
