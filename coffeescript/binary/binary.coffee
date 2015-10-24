class Binary
  constructor: (@binary)->

  toDecimal: ->
    ary = for i in [(@binary.length - 1)..0] by -1
      baseIdx = baseIdx + 1 or 0
      parsedInt = parseInt @binary.charAt i

      if (isNaN parsedInt) or (parsedInt > 1)
        parsedInt = 0

      (parsedInt) * (2 ** baseIdx)

    ary.reduce (sum, elt)->
      sum + elt

module.exports = Binary
