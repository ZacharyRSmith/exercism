class Robot
  @@used_names = { }

  def initialize
    @name = Robot.new_name
  end

  def self.new_name
    name = ('A'..'Z').to_a.shuffle[0,2].join + (0..9).to_a.shuffle[0,3].join
    return Robot.new_name if @@used_names[name]

    @@used_names[name] = true
    name
  end

  def name
    @name
  end

  def reset
    @name = Robot.new_name
  end
end
