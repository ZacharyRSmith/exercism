class Series
  def initialize(sequence)
    @sequence = sequence
  end

  def slices(slice_len)
    if slice_len > @sequence.length
      raise ArgumentError.new("Slice length cannot be larger than sequence.")
    end
    slices = []
    num_slices = @sequence.length - slice_len + 1

    (0...num_slices).each do |i|
      slice = @sequence[i, slice_len]
      slice_ary = slice.split('').inject([]) { |m, ltr| m << ltr.to_i }
      slices << slice_ary
    end

    slices
  end
end
