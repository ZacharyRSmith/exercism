require 'set'


class Sieve
  attr_reader :primes

  def initialize(limit)
    if !limit.is_a?(Integer) || limit < 2
      raise ArgumentError.new("Sieve's limit must be a positive integer above 1")
    end
    @primes = _get_primes_up_to_limit_inclusive(limit)
  end

  private

  def _get_primes_up_to_limit_inclusive(limit)
    primes = [2]
    multiples = Set.new [2]

    (3..limit).step(2) do |n|
      if !multiples.include?(n)
        primes << n
        multiples = _mark_multiples(multiples, n, limit)
      end
    end

    primes
  end

  def _mark_multiples(multiples, start, stop)
    (start..stop).step(start) do |multiple|
      multiples.add(multiple)
    end

    multiples
  end
end
