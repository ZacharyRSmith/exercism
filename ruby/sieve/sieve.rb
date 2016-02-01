#TODO: Refactor to use Set

class Sieve
  attr_reader :primes

  def initialize(limit)
    if !limit.is_a?(Integer) || limit < 2
      raise ArgumentError.new("Sieve's limit must be a positive integer above 1")
    end
    @primes = _gen_primes(limit)
  end

  private

  def _gen_primes(limit)
    primes = [2]
    multiples = { 2 => true }
    crnt = 3

    while crnt <= limit
      if multiples[crnt]
        crnt += 2
        next
      end

      primes << crnt
      multiples = _mark_multiples(multiples, crnt, limit)
      crnt += 2
    end

    primes
  end

  def _mark_multiples(multiples, start, stop)
    # TODO Refactor to use reduce
    multiple = start

    while multiple <= stop
      multiples[multiple] = true
      multiple += start
    end

    multiples
  end
end
