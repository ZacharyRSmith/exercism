class Prime
  @@primes = [2, 3]

  def self.nth(n)
    if n < 1 || !n.is_a?(Integer)
      raise ArgumentError.new('Argument must be a positive integer.')
    end

    while !@@primes[n-1]
      Prime.add_next_prime
    end

    @@primes[n-1]
  end

  def self.add_next_prime
    found = false
    num = @@primes[-1]

    while !found
      if Prime.isnt_multiple_of_cached_primes?(num)
        @@primes << num
        return
      end
      # only check odd numbers
      num += 2
    end
  end

  def self.isnt_multiple_of_cached_primes?(num)
    @@primes.none? { |prime| num % prime == 0 }
  end
end
