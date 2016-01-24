class Hamming
  def self.compute(str1, str2)
    if str1.length != str2.length
      raise ArgumentError.new("Strands must be of equal length")
    end
    
    str1.chars.zip(str2.chars).count {|(a, b)| a != b}
  end
end
