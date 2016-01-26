# Let's break this problem up by looking at each digit's place
# (ie, 1's, 10's, 100's, etc).
# Each digit's place has 3 associated roman numerals:
  # The '1', '5', and '10' numeral.
  # Eg, the 1's place has numerals:
    # '1' => 'I'
    # '5' => 'V'
    # '10' => 'X'
  # and the 10's place has numerals:
    # '1' => 'X'
    # '5' => 'L'
    # '10' => 'C'
# Now, let's say we have a 7 at the 10's place.
# Looking at associated numerals, this converts to:
  # 5 + 1 + 1
  # L + X + X

class Integer
  NUMERALS = {
    1 => {
      1 => 'I',
      5 => 'V',
      10 => 'X'
    },
    10 => {
      1 => 'X',
      5 => 'L',
      10 => 'C'
    },
    100 => {
      1 => 'C',
      5 => 'D',
      10 => 'M'
    },
    1000 => {
      1 => 'M'
    }
  }

  def to_roman
    res = ''
    place = 0

    self.to_s.split('').reverse_each do |num|
      place == 0 ? place = 1 : place *= 10

      # add value from num and place
      res = _get_numerals_of_place(num.to_i, place) + res
    end

    res
  end

  private

    def _get_numerals_of_place(num, place)
      case num
      when 0
        return ''
      when 1..3
        return NUMERALS[place][1] * num
      when 4
        return NUMERALS[place][1] + NUMERALS[place][5]
      when 5
        return NUMERALS[place][5]
      when 6..8
        return NUMERALS[place][5] + NUMERALS[place][1] * (num - 5)
      when 9
        return NUMERALS[place][1] + NUMERALS[place][10]
      end
    end
end


