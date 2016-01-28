class Phrase
  VERSION = 1
  attr_reader :word_count

  def initialize(input)
    @word_count = input.split(/\W+/).reduce({ }) do |memo, word|
      word = word.downcase
      memo[word] ||= 0
      memo[word] += 1
      memo
    end
  end
end
