var _parse = function(int) {
  var num = '' + int;

  if (num.length === 1) {
    num = '0' + num;
  }

  return num;
};

var at = function(hour, min) {
  var result = {
    'hour': hour, 'min': (min || 0)
  };

  result.plus = function(min) {
    result.min += min;

    while (result.min >= 60) {
      result.hour += 1;
      result.min -= 60;
    }
    while (result.hour >= 24) {
      result.hour -= 24;
    }

    return result;
  };

  result.toString = function() {
    return _parse(result.hour) + ':' + _parse(result.min);
  };

  return result;
};


module.exports.at = at;
