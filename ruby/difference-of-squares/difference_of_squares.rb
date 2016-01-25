class Squares
  def initialize(int)
    @int = int
  end

  def square_of_sums
    sums = (@int**2 + @int) / 2
    sums**2
  end

  def sum_of_squares
    (1..@int).reduce(0) { |s, n| s + n**2 }
  end

  def difference
    self.square_of_sums() - self.sum_of_squares()
  end
end
