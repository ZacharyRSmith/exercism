class PrimeFactors
  def self.for(num)
    res = []

    factor = 2
    while factor <= num
      if !_is_factor(num, factor)
        factor = _add_to_factor(factor)
        next
      end

      res << factor
      num /= factor
    end

    res
  end

  # PRIVATE CLASS METHODS

    def self._add_to_factor(factor)
      factor == 2 ? factor += 1 : factor += 2
    end
    private_class_method :_add_to_factor

    def self._is_factor(num, factor)
      num % factor == 0
    end
    private_class_method :_is_factor
end
