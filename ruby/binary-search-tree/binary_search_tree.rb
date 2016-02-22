class Bst
  def initialize(data)
    @data = data
    @children = { }
  end

  attr_reader :data

  def each(&block)
    children['left'].each(&block) unless children['left'].nil?
    yield @data
    children['right'].each(&block) unless children['right'].nil?
  end

  def left
    children['left']
  end
  
  def insert(newData)
    side = (newData > data ? 'right' : 'left')

    if children[side]
      children[side].insert(newData)
    else
      children[side] = self.class.new(newData)
    end
  end

  def right
    children['right']
  end

  private
    attr_reader :children
end
