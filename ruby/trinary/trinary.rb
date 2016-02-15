class Trinary
  INVALID_INPUT_REPLACEMENT = 0.freeze

  def initialize(trinary)
    @decimal = _process_input(trinary)
  end

  @property
  def to_decimal
    decimal
  end

  private
    attr_reader :decimal

    def _process_input(trinary)
      return INVALID_INPUT_REPLACEMENT if /[^0-2]/.match(trinary)

      trinary.reverse.chars.each_with_index.inject(0) do |mem, (ltr, i)|
        n = ltr.to_i
        val = n * 3**i
        mem += val
      end
    end
end
