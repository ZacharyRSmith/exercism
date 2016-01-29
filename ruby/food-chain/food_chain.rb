class FoodChain
  VERSION = 2

  def self.song
    song = ""

    for i in 1..7
      song += _verse(i) + "\n"
    end

    song += _ending
  end

  private

    def self._ending
      "I know an old lady who swallowed a horse.\n" +
      "She's dead, of course!\n"
    end

    def self._first_verse_lines(verse_num)
      if verse_num == 1
        _first_verse_line("fly")
      elsif verse_num == 2
        _first_verse_line("spider") +
        "It wriggled and jiggled and tickled inside her.\n"
      elsif verse_num == 3
        _first_verse_line("bird") +
        "How absurd to swallow a bird!\n"
      elsif verse_num == 4
        _first_verse_line("cat") +
        "Imagine that, to swallow a cat!\n"
      elsif verse_num == 5
        _first_verse_line("dog") +
        "What a hog, to swallow a dog!\n"
      elsif verse_num == 6
        _first_verse_line("goat") +
        "Just opened her throat and swallowed a goat!\n"
      elsif verse_num == 7
        _first_verse_line("cow") +
        "I don't know how she swallowed a cow!\n"
      end
    end

    def self._repeated_lines(verse_num)
      repeated_lines = ""

      repeated_lines += "She swallowed the cow to catch the goat.\n" if verse_num > 6
      repeated_lines += "She swallowed the goat to catch the dog.\n" if verse_num > 5
      repeated_lines += "She swallowed the dog to catch the cat.\n" if verse_num > 4
      repeated_lines += "She swallowed the cat to catch the bird.\n" if verse_num > 3
      repeated_lines += "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.\n" if verse_num > 2
      repeated_lines += "She swallowed the spider to catch the fly.\n" if verse_num > 1
      repeated_lines += "I don't know why she swallowed the fly. Perhaps she'll die.\n"

      repeated_lines
    end

    def self._verse(verse_num)
      verse = ""

      verse += _first_verse_lines(verse_num)
      verse += _repeated_lines(verse_num)

      verse
    end

    def self._first_verse_line(animal)
      "I know an old lady who swallowed a #{animal}.\n"
    end
end

puts FoodChain.song
