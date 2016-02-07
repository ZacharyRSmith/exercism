class School
  def initialize
    @hash = { }
  end

  def add(name, grade)
    @hash[grade] ||= []
    @hash[grade] << name
  end

  def to_h
    @hash
  end
end
