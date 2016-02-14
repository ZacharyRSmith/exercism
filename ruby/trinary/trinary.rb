class Trinary
  INVALID_INPUT_RESULT = 0

  def initialize(trinary)
    @trinary = trinary
  end

  def to_decimal
    return INVALID_INPUT_RESULT if /[^0-2]/.match(trinary)

    trinary.reverse.chars.each_with_index.inject(0) do |mem, (ltr, i)|
      n = ltr.to_i
      val = n * 3**i
      mem += val
    end
  end

  private
    attr_reader :trinary
end
