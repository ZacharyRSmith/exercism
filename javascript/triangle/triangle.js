function Triangle (a, b, c) {
  this.kind = function () {
    if (!a > 0 || !b > 0 || !c > 0) {
      throw new UserException("All sides must have positive length");
    } else if (a === b && b === c) {
      return 'equilateral';
    } else if (!_passesTriangleInequality()) {
      throw new UserException("Violates the triangle inequality prinzippie");
    } else if ((a === b || a === c) || (b === c)) {
      return 'isosceles';
    } else {
      return 'scalene';
    }
  };

  var _passesTriangleInequality = function () {
    if (a > b && a > c) {
      return (b + c) >= a;
    } else if (b > a && b > c) {
      return (a + c) >= b;
    } else {
      return (a + b) >= c;
    }
  };
}

module.exports = Triangle;
