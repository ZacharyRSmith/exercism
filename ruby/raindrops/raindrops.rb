class Raindrops
  SOUNDS_MAP = {
    3 => "Pling",
    5 => "Plang",
    7 => "Plong"
  }

  def self.convert(int)
    sound = SOUNDS_MAP.map do |factor, factor_sound|
      SOUNDS_MAP[factor] if int % factor == 0
    end.compact

    sound.empty? ? String(int) : sound.join('')
  end
end
