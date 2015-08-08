function isLeapYear (int) {
  if (int % 4 === 0 && (int % 100 !== 0 || int % 400 === 0)) { return true; }
  else { return false; }
}

// on every year that is evenly divisible by 4
//   except every year that is evenly divisible by 100
//     unless the year is also evenly divisible by 400

module.exports = isLeapYear;
