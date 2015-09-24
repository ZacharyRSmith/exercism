var bufferEmptyException = function () {
  return {
    name: "bufferEmptyException",
    message: "Cannot perform requested operation because the buffer is empty!",
    toString: function () {
      return this.name + ": " + this.message;
    } 
  };
};

var bufferFullException = function () {
  return {
    name: "bufferFullException",
    message: "Cannot write to a full buffer!",
    toString: function () {
      return this.name + ": " + this.message;
    } 
  };
};

var circularBuffer = function (size) {
  var buffer = new Array(size);

  var next = 0;
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
      return elt == undefined;
    });
  };

  buffer._isFull = function () {
    return (next === oldest) && buffer[next] !== undefined;
  };

  buffer.clear = function () {
    next = 0;
    oldest = 0;
    for (var i = 0; i < buffer.length; i++) {
      buffer[i] = undefined;
    }
  };

  buffer.forceWrite = function (input) {
    if (input == null) {
      return;
    }
    if (next === oldest) {
      oldest = _increment(oldest);
    }
    buffer[next] = input;
    next = _increment(next);
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
    if (input == null) {
      return;
    }
    if (buffer._isFull()) {
      throw new bufferFullException();
    }
    buffer[next] = input;
    next = _increment(next);
  };

  return buffer;
};


module.exports.circularBuffer = circularBuffer;
module.exports.bufferEmptyException = bufferEmptyException;
module.exports.bufferFullException = bufferFullException;
