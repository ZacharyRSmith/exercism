class Binary
  VERSION = 1

  def initialize(str)
    if str.match(/[^0-1]/)
      raise ArgumentError.new("Binary string must contain only 1's and 0's.")
    end
    @str = str
  end

  def to_decimal
    sum = 0
    reversed = @str.reverse

    (0..reversed.length-1).each do |i|
      next if reversed[i] == "0"
      sum += 2**(i)
    end

    sum
  end
end
