class Bst
  def initialize(data)
    @data = data
    @children = { }
  end

  attr_reader :data

  def each(&block)
    @children['left'].each(&block) if @children['left']
    yield @data
    @children['right'].each(&block) if @children['right']
  end

  def left
    @children['left']
  end
  
  def insert(newData)
    side = (newData > data ? 'right' : 'left')

    if @children[side]
      @children[side].insert(newData)
    else
      @children[side] = self.class.new(newData)
    end
  end

  def right
    @children['right']
  end
end
