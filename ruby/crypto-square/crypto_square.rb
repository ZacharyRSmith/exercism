class Crypto
  def initialize(original)
    @original = original
  end

  def ciphertext()
    segments = plaintext_segments()
    segments.inject(Array.new(segments.length)) do |cipher, seg|
      seg.chars.each_with_index do |char, i|
        cipher[i] ||= []
        cipher[i] << char
      end
      cipher
    end.join('')
  end

  def normalize_plaintext() original.gsub(/\W/, '').downcase end

  def plaintext_segments()
    chars = normalize_plaintext()
    seg_size = size()
    # The "." matches any character
    # The "{1,n}" greedily grabs between 1 and n characters
    chars.scan(/.{1,#{seg_size}}/)
  end

  def size()
    num_chars = normalize_plaintext().size
    Math.sqrt(num_chars).ceil
  end
  
  private
    attr_reader :original
end