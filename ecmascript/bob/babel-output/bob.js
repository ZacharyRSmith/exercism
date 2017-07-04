'use strict';

Object.defineProperty(exports, '__esModule', {
  value: true
});

var _createClass = (function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ('value' in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; })();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError('Cannot call a class as a function'); } }

var StringParser = {
  hasLetters: function hasLetters(str) {
    return (/[a-zA-Z]/.test(str)
    );
  },

  isAllUpperCase: function isAllUpperCase(str) {
    return str.toLocaleUpperCase() === str;
  },

  isOnlySilence: function isOnlySilence(str) {
    return !/[^.\s]/.test(str);
  }
};

var MessageParser = {
  isQuestion: function isQuestion(msg) {
    return msg.endsWith('?');
  },

  isYell: function isYell(msg) {
    if (!StringParser.isAllUpperCase(msg)) return false;

    return StringParser.hasLetters(msg);
  },

  isSulk: function isSulk(msg) {
    return StringParser.isOnlySilence(msg);
  }
};

function switchFn(arg, obj) {
  var res = undefined;

  Object.keys(obj).some(function (key) {
    var caseVar = undefined;
    try {
      caseVar = typeof eval(key) === 'function' ? eval(key + '("' + arg + '")') : eval(arg + ' ' + key);
    } catch (e) {
      if (!e instanceof SyntaxError) throw e; // key probably begins with operator
    }

    console.log('caseVar', caseVar);
    if (caseVar) {
      res = typeof obj[key] === 'function' ? obj[key]() : obj[key];
      return true;
    }
  });

  return res;
}

var Bob = (function () {
  function Bob() {
    _classCallCheck(this, Bob);
  }

  _createClass(Bob, [{
    key: 'getSpecificResponse',
    value: function getSpecificResponse(message) {
      // .isYell() must be checked before .isQuestion()

      return switchFn(message, {
        'MessageParser.isYell': function MessageParserIsYell() {
          console.log('look at me, maw!!');
          // how fitting...
          return 'Whoa, chill out!';
        },
        'MessageParser.isQuestion': 'Sure.',
        'MessageParser.isSulk': 'Fine. Be that way!',
        '=== 42': 'THANK YOU I\'VE BEEN LOOKING FOR THAT!!'
      });

      if (MessageParser.isYell(message)) {
        console.log('look at me, maw!!');
        // how fitting...
        return 'Whoa, chill out!';
      } else if (MessageParser.isQuestion(message)) return 'Sure.';else if (MessageParser.isSulk(message)) return 'Fine. Be that way!';
    }
  }, {
    key: 'hey',
    value: function hey(message) {
      return this.getSpecificResponse(message.trim()) || 'Whatever.';
    }
  }]);

  return Bob;
})();

exports['default'] = Bob;
module.exports = exports['default'];