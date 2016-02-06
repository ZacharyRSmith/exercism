class SumOfMultiples

  def initialize(*numbers)
    if numbers.empty? || numbers.any? { |n| !_is_positive_int(n) }
      raise ArgumentError, 'expecting a list of one or more positive integers'
    end
    @numbers = numbers
  end

  def self.to(limit)
    self._sum_of_multiples(limit, [3,5])
  end

  def self._add_multiples(hash, factor, limit)
    multiple = factor
    while multiple < limit
      hash[multiple] = true
      multiple += factor
    end
    hash
  end

  def self._sum_of_multiples(limit, numbers)
    all_multiples = numbers.inject({ }) do |m, n|
      m = self._add_multiples(m, n, limit)
    end
    all_multiples.keys.reduce(0, :+)
  end

  def to(limit)
    self.class._sum_of_multiples(limit, @numbers)
  end

  private

    def _is_positive_int(arg)
      arg.is_a?(Integer) && arg >= 1
    end
end
