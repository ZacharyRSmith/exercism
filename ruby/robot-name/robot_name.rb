class Robot
  @@used_names = { }

  attr_reader :name
  def initialize
    @name = Robot.gen_name
  end

  def self.gen_name
    name = ''
    2.times { name << [*'A'..'Z'].sample }
    name << "%03d" % rand(0..999)
    return Robot.gen_name if @@used_names[name]

    @@used_names[name] = true
    name
  end

  def reset
    @@used_names.delete(@name)
    @name = Robot.gen_name
  end
end
