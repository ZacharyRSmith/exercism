class School
  VERSION = 1

  def initialize
    @hash = { }
  end

  def add(name, grade)
    @hash[grade] ||= []
    @hash[grade] << name
    @hash[grade].sort!
  end

  def grade(grade)
    @hash[grade] ||= []
  end

  def to_h
    Hash[@hash.sort]
  end
end
