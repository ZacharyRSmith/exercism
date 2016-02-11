class Array
  def discard
    self.delete_if { |e| yield(e) }
  end

  def keep(&predicate)
    # CHEATING SOLUTION 1
    # self.delete_if { |e| !yield(e) }

    # CHEATING SOLUTION 2
    # new_ary = []

    # self.each do |e|
    #   new_ary << e if yield(e)
    # end

    # self.replace new_ary

    new_ary = []

    (0...self.size).each do |i|
      new_ary << self[i] if yield(self[i])
    end

    self.replace new_ary
  end
end
