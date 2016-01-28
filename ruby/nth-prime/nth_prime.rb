class Prime

  def self.nth(n)
    if n < 1 || !n.is_a?(Integer)
      raise ArgumentError.new('Argument must be a positive integer.')
    end

    while !cache[n-1]
      Prime.add_next_prime
    end

    cache[n-1]
  end

  def self.add_next_prime
    num = cache.last

    loop do
      if Prime.isnt_multiple_of_cached_primes?(num)
        cache << num
        return
      end
      # only check odd numbers
      num += 2
    end
  end

  def self.isnt_multiple_of_cached_primes?(num)
    cache.none? { |prime| num % prime == 0 }
  end

  private

    def self.cache
      @primes ||= [2, 3]
    end
end
