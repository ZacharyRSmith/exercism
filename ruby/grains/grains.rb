class Grains

  def self.square(num)
    # naive solution
    sum = 0

    for i in 1...num
      sum += sum + 1
    end

    sum + 1
  end

  def self.total
    square(64) * 2 - 1
  end
end
