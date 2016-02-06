class Array
  def accumulate(&cb)
    res = []

    self.my_each { |e| res << cb.call(e) }

    res
  end

  def my_each
    for e in self
      yield e
    end
  end
end
