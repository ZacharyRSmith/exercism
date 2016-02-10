class PhoneNumber
  INVALID_NUMBER = '0000000000'
  JUST_TEN_DIGITS = /\A\d{10}\z/

  def initialize(number)
    @number = _clean_number(number)
  end

  attr_reader :number

  @property
  def area_code
    number[0, 3]
  end

  @property
  def exchange_number
    number[3, 3]
  end

  @property
  def subscriber_number
    number[6, 4]
  end

  def to_s
    format "(%03d) %03d-%04d", area_code, exchange_number, subscriber_number
  end

  private

    def _clean_number(str)
      digits = _remove_punct_and_space(str)
      digits = _remove_leading_1(digits)
      return INVALID_NUMBER if digits !~ JUST_TEN_DIGITS

      digits
    end

    def _remove_leading_1(str)
      if str.size == 11 && str[0] == '1'
        return str[1..str.size]
      else
        return str
      end
    end

    def _remove_punct_and_space(str)
      str.gsub(/[[:punct:][:space:]]/, '')
    end
end