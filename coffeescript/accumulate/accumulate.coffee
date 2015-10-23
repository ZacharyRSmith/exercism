Array.prototype.accumulate = (accumulator)->
    res = []

    for elt in @
        res.push accumulator elt

    res

module.exports = Array.prototype.accumulate
