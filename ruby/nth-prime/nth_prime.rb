class Prime
  def self.nth(n)
    if n < 1 || !n.is_a?(Integer)
      raise ArgumentError.new('Argument must be a positive integer.')
    end
    # alt solution:
    # could create a set of numbers, from which we'd remove multiples of primes

    # naive solution:
    i = 2
    nth = 0
    primes = []
    while nth < n
      if primes.none? { |prime| i % prime == 0 }
        primes << i
        nth += 1
      end

      i += 1
    end

    primes.pop
  end
end
