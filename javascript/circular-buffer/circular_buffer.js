var bufferEmptyException = function () {
  return {
    name: "bufferEmptyException",
    message: "Cannot perform requested operation because the buffer is empty!",
    toString: function () {
      return this.name + ": " + this.message;
    } 
  };
};

var circularBuffer = function (size) {
  var buffer = new Array(size);

  var newest = 0;
  var oldest = 0;

  var _increment = function (index) {
    index += 1;

    if (index === buffer.length) {
      index = 0;
    }

    return index;
  };

  buffer._isEmpty = function () {
    return buffer.every(function (elt) {
      return elt === undefined;
    });
  };

  buffer.clear = function () {
    newest = 0;
    oldest = 0;
    buffer.every(function (elt) {
      elt = undefined;
    });
  };

  buffer.read = function () {
    if (buffer._isEmpty()) {
      throw new bufferEmptyException();
    }
    var val = buffer[oldest];
    buffer[oldest] = undefined;
    oldest = _increment(oldest);

    return val;
  };

  buffer.write = function (input) {
    buffer[newest] = input;
    newest = _increment(newest);
  };

  return buffer;
};


module.exports.circularBuffer = circularBuffer;
module.exports.bufferEmptyException = bufferEmptyException;
// module.exports.bufferFullException = bufferFullException;
