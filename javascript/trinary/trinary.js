function Trinary(str) {
  if ((/[^0-2]/).test(str)) {
    str = '0';
  }
  this.digs = str.split('');
}
Trinary.prototype.toDecimal = function() {
  return this.digs.reverse().reduce(function(sum, crnt, i) {
    return sum + (crnt * Math.pow(3, i));
  }, 0);
};

module.exports = Trinary;
