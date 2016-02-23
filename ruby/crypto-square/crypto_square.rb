class Crypto
  def initialize(original)
    @original = original
  end

  def normalize_plaintext
    original.gsub(/\W/, '').downcase
    # original.gsub(/[[:punct:][:space:]]/, '')
  end
  
  private
    attr_reader :original
end