'use strict';

Object.defineProperty(exports, '__esModule', {
    value: true
});

var _createClass = (function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ('value' in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; })();

function _toConsumableArray(arr) { if (Array.isArray(arr)) { for (var i = 0, arr2 = Array(arr.length); i < arr.length; i++) arr2[i] = arr[i]; return arr2; } else { return Array.from(arr); } }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError('Cannot call a class as a function'); } }

function transcribe(_ref) {
    var nucleotide = _ref.nucleotide;
    var complements = _ref.complements;

    if (!complements[nucleotide]) throw new Error('Invalid nucleotide "' + nucleotide + '" given!');
    return complements[nucleotide];
}

var DnaTranscriber = (function () {
    function DnaTranscriber() {
        _classCallCheck(this, DnaTranscriber);

        this.complements = DnaTranscriber.complements;
    }

    _createClass(DnaTranscriber, [{
        key: 'toRna',
        value: function toRna(dnaStrand) {
            var complements = this.complements;

            return [].concat(_toConsumableArray(dnaStrand)).reduce(function (val, nucleotide) {
                return val + transcribe({ nucleotide: nucleotide, complements: complements });
            }, '');
        }
    }]);

    return DnaTranscriber;
})();

DnaTranscriber.complements = {
    'A': 'U',
    'T': 'A',
    'C': 'G',
    'G': 'C'
};

exports['default'] = DnaTranscriber;
module.exports = exports['default'];