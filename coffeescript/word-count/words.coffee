class Words
  constructor: (input) ->
    @input = input

  count: ->
    res = { }

    for word in @input.replace(/[^\w\s]/g, "").toLowerCase().split(/[\s]+/)
      if not res[word]
        res[word] = 0

      res[word] += 1

    res

module.exports = Words
