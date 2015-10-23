class Bob
  hey: (prompt) ->
    response = if prompt.toUpperCase() is prompt and /[a-zA-Z]/.test(prompt)
      "Whoa, chill out!"
    else if prompt.endsWith("?")
      "Sure."
    else if prompt.trim() is ""
      "Fine. Be that way!"
    else
      "Whatever."

    response

module.exports = Bob
