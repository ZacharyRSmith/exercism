class School
  VERSION = 1

  def initialize
    @db = Hash.new { |hash, key| hash[key] = [] }
  end

  def add(name, grade)
    db[grade] << name
    db[grade].sort!
  end

  def grade(grade)
    db[grade]
  end

  def to_h
    Hash[db.sort]
  end

  private

    attr_reader :db
end
