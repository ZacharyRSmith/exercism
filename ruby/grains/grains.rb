class Grains
  def self.board
    @board = (1..64).map { |sqr| 2**(sqr-1) }
  end

  def self.square(n)
    board[n-1]
  end

  def self.total
    board.reduce(:+)
  end
end
