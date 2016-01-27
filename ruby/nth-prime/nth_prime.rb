class Prime
  @@primes = [2]

  def self.nth(n)
    if n < 1 || !n.is_a?(Integer)
      raise ArgumentError.new('Argument must be a positive integer.')
    end

    return @@primes[n-1] if @@primes[n-1]

    # alt solution:
    # could create a set of numbers, from which we'd remove multiples of primes

    # naive solution:
    num = @@primes[-1]
    while !@@primes[n-1]
      @@primes << num if Prime.isnt_multiple_of_cached_primes?(num)

      num += 1
    end

    @@primes[-1]
  end

  def self.isnt_multiple_of_cached_primes?(num)
    @@primes.none? { |prime| num % prime == 0 }
  end
end
