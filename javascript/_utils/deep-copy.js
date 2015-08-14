module.exports = function deepCopy(arg) {
  var copy, props;

  if (arg instanceof Object) {
//     if (arg instanceof Array) {
//       copy = []
//     }
//     else {
      copy = Object.create(Object.getPrototypeOf(arg));
//     }

    props = Object.getOwnPropertyNames(arg);

    props.forEach(function (prop) {
            copy[prop] = deepCopy(arg[prop]);
    });

    return copy;
  }
  else { return arg; }
};
