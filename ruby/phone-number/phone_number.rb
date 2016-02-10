class PhoneNumber
  def initialize(number)
    @number = _clean_number(number)
  end

  attr_reader :number

  @property
  def area_code
    "#{number[0..2]}"
  end

  @property
  def subscriber_number
    "#{number[3..5]}-#{number[6..9]}"
  end

  def to_s
    "(#{area_code}) #{subscriber_number}"
  end

  private

    def _clean_number(str)
      return '0000000000' if str.match(/[a-zA-Z]/)

      digits = str.gsub(/\D/, '')
      return '0000000000' if digits.size < 10
      return '0000000000' if digits.size > 11

      if digits.size == 11
        if digits[0] == '1'
          return digits[1..digits.size]
        else
          return '0000000000'
        end
      end

      digits
    end
end
