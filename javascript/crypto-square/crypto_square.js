function Crypto(plaintext) {
  this.plaintext = plaintext;

  this.ciphertext = function() {
    var ptextSegs = this.plaintextSegments();
    var result = '';

    for (var i = 0; i < ptextSegs.length; i++) {
      ptextSegs.forEach(function(seg) {
        result += seg.substr(i, 1);
      });
    }
    return result;
  };
BUG
  this.normalizeCiphertext = function() {
    return this.ciphertext();
  };

  this.normalizePlaintext = function() {
    return this.plaintext.toLowerCase().replace(/\W/g, '');
  };

  this.plaintextSegments = function() {
    var plaintext = this.normalizePlaintext();
    var result = [];
    var segLen = this.size();

    for (var i = 0; i < plaintext.length; i += segLen) {
      result.push(plaintext.substr(i, segLen));
    }
    return result;
  };

  this.size = function() {
    var sqrt = Math.sqrt(this.normalizePlaintext().length);

    if (sqrt % 1 > 0) {
      return Math.floor(sqrt) + 1;
    } else {
      return sqrt;
    }
  };
}

module.exports = Crypto;
