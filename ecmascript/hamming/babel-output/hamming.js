'use strict';

Object.defineProperty(exports, '__esModule', {
  value: true
});

var _createClass = (function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ('value' in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; })();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError('Cannot call a class as a function'); } }

var Hamming = (function () {
  function Hamming() {
    _classCallCheck(this, Hamming);
  }

  _createClass(Hamming, [{
    key: 'compute',
    value: function compute(strand1, strand2) {
      if (strand1.length !== strand2.length) throw new Error('DNA strands must be of equal length.');

      return strand1.split('').reduce(function (counter, acid, i) {
        if (acid === strand2[i]) return counter;else return counter += 1;
        // return counter += ( acid !== strand2[i] ? 1 : 0 )
      }, 0);
    }
  }]);

  return Hamming;
})();

exports['default'] = Hamming;

// export default class Hamming {
//   compute(a, b) {
//     if(a.length !== b.length) throw new Error('DNA strands must be of equal length.');

//     for(let e of String(a).entries()) {
//       console.log(e)
//     }

//     // return a.split('').reduce((memo, _, idx) => {
//     //   return (a[idx] === b[idx] ? memo : ++memo);
//     // }, 0)
//   }
// };
module.exports = exports['default'];