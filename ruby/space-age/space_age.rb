class SpaceAge
  SECONDS_PER_EARTH_YEAR = 31557600
  # mapping of earth years per orbital period
  PERIOD_CONVERSIONS = {
    'earth' => 1,
    'mercury' => 0.2408467,
    'venus' => 0.61519726,
    'mars' => 1.8808158,
    'jupiter' => 11.862615,
    'saturn' => 29.447498,
    'uranus' => 84.016846,
    'neptune' => 164.79132
  }

  attr_reader :seconds

  def initialize(seconds)
    @seconds = seconds
  end

  PERIOD_CONVERSIONS.each do |planet, ratio|
    define_method("on_#{planet}") do
      seconds.to_f / (SECONDS_PER_EARTH_YEAR * PERIOD_CONVERSIONS[planet])
    end
  end
end
