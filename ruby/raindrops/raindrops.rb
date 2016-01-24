class Raindrops
  def self.convert(int)
    sound = ''

    if int % 3 == 0
      sound += 'Pling'
    end
    if int % 5 == 0
      sound += 'Plang'
    end
    if int % 7 == 0
      sound += 'Plong'
    end

    sound.empty? ? String(int) : sound
  end
end
