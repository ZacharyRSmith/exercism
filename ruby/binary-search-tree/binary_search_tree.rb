class Bst
  def initialize(data)
    @data = data
    @leftChild = nil
    @rightChild = nil
  end

  attr_reader :data

  def each(&block)
    @leftChild.each(&block) if @leftChild
    yield @data
    @rightChild.each(&block) if @rightChild
  end

  def left
    @leftChild
  end
  
  def insert(newData)
    if newData > data
      if @rightChild
        @rightChild.insert(newData)
      else
        @rightChild = self.class.new(newData)
      end
    else
      if @leftChild
        @leftChild.insert(newData)
      else
        @leftChild = self.class.new(newData)
      end
    end
  end

  def right
    @rightChild
  end
end
