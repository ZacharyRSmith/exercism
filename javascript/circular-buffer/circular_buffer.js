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

  buffer.isEmpty = function () {
    return buffer.every(function (elt) {
      return elt === undefined;
    });
  };

  buffer.read = function () {
    if (buffer.isEmpty()) {
      throw new bufferEmptyException();
    }
  };

  return buffer;
};


module.exports.circularBuffer = circularBuffer;
module.exports.bufferEmptyException = bufferEmptyException;
// module.exports.bufferFullException = bufferFullException;
