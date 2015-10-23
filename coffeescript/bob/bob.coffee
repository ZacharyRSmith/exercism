class Bob
  hey: (greeting)->
    if greeting.toUpperCase() is greeting and /[a-zA-Z]/.test(greeting)
      return "Whoa, chill out!"
    if greeting.substr(-1) is "?"
      return "Sure."
    if greeting.trim() is ""
      return "Fine. Be that way!"

    "Whatever."

module.exports = Bob
