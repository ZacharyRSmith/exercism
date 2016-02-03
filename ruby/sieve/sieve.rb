require 'set'


class Sieve
  attr_reader :primes

  def initialize(limit)
    if !limit.is_a?(Integer) || limit < 2
      raise ArgumentError.new("Sieve's limit must be a positive integer above 1")
    end
    @primes = _gen_primes_up_to_limit_inclusive(limit)
  end

  private

  def _gen_primes_up_to_limit_inclusive(limit)
    candidates = Set.new [2]
    # Add all odd numbers from 3 to limit inclusive
    candidates.merge((3..limit).step(2).to_a)

    candidates.each do |candidate|
      _remove_multiples(candidates, candidate)
    end

    candidates.to_a
  end

  def _remove_multiples(candiates, n)
    ((2*n)..limit).step(n) { |multiple| candidates.delete(multiple) }
  end
end
