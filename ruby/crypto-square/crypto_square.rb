class Crypto
  def initialize(original)
    @original = original
  end

  def normalize_plaintext() original.gsub(/\W/, '').downcase end

  def size
    num_chars = normalize_plaintext().size
    Math.sqrt(num_chars).ceil
  end
  
  private
    attr_reader :original
end