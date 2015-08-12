function Triangle (a, b, c) {
  this.kind = function () {
    if (a <= 0 || a > (b+c) ||
        b <= 0 || b > (a+c) ||
        c <= 0 || c > (a+b)) {
      throw new UserException('Illegal triangle');
    }

    if (a === b && b === c) {
      return 'equilateral';
    }
    else if (a === b || a === c || b === c) {
      return 'isosceles';
    }
    else {
      return 'scalene';
    }
  };
}

module.exports = Triangle;
