def slices(series, size):
    if not size > 0:
        raise ValueError("Your size argument must be an integer greater "
                         "than 0! ;_;")
    if size > len(series):
        raise ValueError("Your size argument cannot be larger than the "
                         "series' length. Sneak!")

    nums = [int(n) for n in series]

    return [nums[i:i+size]
            for i in xrange(len(nums)+1 - size)]
