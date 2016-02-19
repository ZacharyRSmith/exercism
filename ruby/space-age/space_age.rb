class SpaceAge
  SECONDS_PER_EARTH_YEAR = 31557600
  # mapping of earth years per orbital period
  PERIOD_CONVERSIONS = {
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

  def on_earth
    seconds / SECONDS_PER_EARTH_YEAR.to_f
  end

  def on_jupiter
    on_earth / PERIOD_CONVERSIONS['jupiter']
  end

  def on_mars
    on_earth / PERIOD_CONVERSIONS['mars']
  end

  def on_mercury
    on_earth / PERIOD_CONVERSIONS['mercury']
  end

  def on_neptune
    on_earth / PERIOD_CONVERSIONS['neptune']
  end

  def on_saturn
    on_earth / PERIOD_CONVERSIONS['saturn']
  end

  def on_uranus
    on_earth / PERIOD_CONVERSIONS['uranus']
  end

  def on_venus
    on_earth / PERIOD_CONVERSIONS['venus']
  end
end
