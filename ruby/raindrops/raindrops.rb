class Raindrops
  SOUNDS_MAP = {
    3 => "Pling",
    5 => "Plang",
    7 => "Plong"
  }

  def self.convert(int)
    sound = ''

    SOUNDS_MAP.each_key do |factor|
      if int % factor == 0
        sound += SOUNDS_MAP[factor]
      end
    end

    sound.empty? ? String(int) : sound
  end
end
