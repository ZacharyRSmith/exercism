const StringParser = {
  hasLetters: (str) => {
    return /[a-zA-Z]/.test(str);
  },

  isAllUpperCase: (str) => {
    return str.toLocaleUpperCase() === str;
  },

  isOnlySilence: (str) => {
    return !/[^.\s]/.test(str);
  }
};

const MessageParser = {
  isQuestion: (msg) => {
    return msg.endsWith('?');
  },

  isYell: (msg) => {
    if(!StringParser.isAllUpperCase(msg)) return false;

    return StringParser.hasLetters(msg);
  },

  isSulk: (msg) => {
    return StringParser.isOnlySilence(msg);
  }
};


function switchFn (arg, obj) {
  let res;

  Object.keys(obj).some((key) => {
    let caseVar;
    try {
      caseVar = typeof eval(key) === 'function'
        ? eval(`${key}("${arg}")`)
        : eval(`${arg} ${key}`);
    } catch(e) {
      if (!e instanceof SyntaxError) throw e; // key begins with operator?
    }

    if (caseVar) {
      res = ( typeof obj[key] === 'function' ? obj[key]() : obj[key] )
      return true;
    }
  });

  return res;
}

export default class Bob {
  getSpecificResponse(message) {
    // .isYell() must be checked before .isQuestion()

    return switchFn(message, {
      'MessageParser.isYell': () => {
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
    } else if (MessageParser.isQuestion(message)) return 'Sure.';
    else if (MessageParser.isSulk(message)) return 'Fine. Be that way!';
  }

  hey(message) {
    return this.getSpecificResponse(message.trim()) || 'Whatever.';
  }
}
