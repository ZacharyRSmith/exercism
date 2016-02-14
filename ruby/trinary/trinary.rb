class Trinary
  INVALID_INPUT_RESULT = 0

  def initialize(trinary)
    @trinary = trinary
  end

  def to_decimal
    return INVALID_INPUT_RESULT if /[^0-2]/.match(trinary)

    i = -1
    trinary.reverse.each_char.inject(0) do |mem, ltr|
      i += 1
      n = ltr.to_i
      mem += (n * 3**i)
    end
  end

  private
    attr_reader :trinary
end
