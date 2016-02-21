class Anagram
  def initialize(original_word)
    @original_word_normalized = _normalize(original_word)
    @original_word_sorted = _sort(original_word_normalized)
  end

  def match(candidates) candidates.select { |c| _is_anagram?(c) } end

  private
    attr_reader :original_word_normalized
    attr_reader :original_word_sorted

    def _is_anagram?(candidate)
      candidate_normalized = _normalize(candidate)
      return candidate_normalized != original_word_normalized &&
          _sort(candidate_normalized) == original_word_sorted
    end

    def _normalize(arg) arg.downcase end

    def _sort(word) word.chars.sort end
end
