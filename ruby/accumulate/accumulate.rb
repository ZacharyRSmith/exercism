class Array
  def accumulate(&cb)
    res = []

    self.each { |e| res << cb.call(e) }

    res
  end
end
