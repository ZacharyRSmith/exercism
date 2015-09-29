var alpha = 'abcdefghijklmnopqrstuvwxyz'.split('');
var revAlpha = alpha.slice().reverse(); 

function _encodeChar(char) {
  if (!isNaN(char)) {
    return char;
  }
  var regI = alpha.indexOf(char.toLowerCase()) ;
  return revAlpha[regI];
}

module.exports = {
  encode: function(input) {
    str = input.replace(/\W/g, '');

    return str.split('').reduce(function(encodedStr, crntChar, i) {
      if (i % 5 === 0 && i !== 0) {
        encodedStr += ' ';
      }
      return encodedStr += _encodeChar(crntChar);
    }, '');
  }
};
