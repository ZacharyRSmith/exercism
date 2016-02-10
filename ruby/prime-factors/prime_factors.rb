class PrimeFactors

  def self.for(num)
    factors = []

    factor = 2
    while factor <= num
      if !_is_factor(num, factor)
        factor = _add_to_factor(factor)
        next
      end

      factors << factor
      num /= factor
    end

    factors
  end

  # PRIVATE CLASS METHODS

    def self._add_to_factor(factor)
      factor == 2 ? factor += 1 : factor += 2
    end
    private_class_method :_add_to_factor

    def self._is_factor(num, factor)
      (num % factor).zero?
    end
    private_class_method :_is_factor
end
