"use strict";
var HelloWorld = $traceurRuntime.initTailRecursiveFunction(function() {
  return $traceurRuntime.call(function() {
    function HelloWorld() {}
    return $traceurRuntime.continuation($traceurRuntime.createClass, $traceurRuntime, [HelloWorld, {hello: function() {
        var name = arguments[0] !== (void 0) ? arguments[0] : 'world';
        return ("Hello, " + name + "!");
      }}, {}]);
  }, this, arguments);
})();
var $__default = HelloWorld;
Object.defineProperties(module.exports, {
  default: {get: function() {
      return $__default;
    }},
  __esModule: {value: true}
});
