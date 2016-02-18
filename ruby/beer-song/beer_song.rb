class BeerSong
  VERSION = 2

  def lyrics
    verses(99, 0)
  end

  def verse(num)
    _get_verse(num)
  end

  def verses(start, stop)
    raise ArgumentError.new("Last verse must be after first verse") if stop > start

    start.downto(stop).inject([]) { |mem, num| mem << _get_verse(num) }.join("\n")
  end

  private
    def _get_verse(num)
      if num > 1
        return "#{num} bottles of beer on the wall, #{num} bottles of beer.\n" \
               "Take one down and pass it around, #{num - 1} #{num - 1 == 1 ? "bottle" : "bottles"} of beer on the wall.\n"
      elsif num == 1
        return "1 bottle of beer on the wall, 1 bottle of beer.\n" \
               "Take it down and pass it around, no more bottles of beer on the wall.\n"
      elsif num == 0
        return "No more bottles of beer on the wall, no more bottles of beer.\n" \
               "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
      end
    end
end
