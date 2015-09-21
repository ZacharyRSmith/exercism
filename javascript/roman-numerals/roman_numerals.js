function getPlace(place, int) {
  if (int === 0) {
    return '';
  }

  var one, five, ten;

  switch (place) {
    case 1:
      one = 'I';
      five = 'V';
      ten = 'X';
      break;
    case 2:
      one = 'X';
      five = 'L';
      ten = 'C';
      break;
    case 3:
      one = 'C';
      five = 'D';
      ten = 'M';
      break;
    case 4:
      one = 'M';
      break;
  }

  switch (int) {
    case 9:
      return one + ten;
    case 8:
      return five + one + one + one;
    case 7:
      return five + one + one;
    case 6:
      return five + one;
    case 5:
      return five;
    case 4:
      return one + five;
    case 3:
      return one + one + one;
    case 2:
      return one + one;
    case 1:
      return one;
  }
}

module.exports = function(num) {
  var int;
  var place = 1;
  var result = '';

  while (num >= 1) {
    int = num % 10;
    result = getPlace(place, int) + result;
    place += 1;
    num = Math.floor(num /= 10);
  }

  return result;
};
