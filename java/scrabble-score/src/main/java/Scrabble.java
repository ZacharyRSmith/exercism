import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static java.lang.Character.toUpperCase;
import static java.util.Arrays.asList;
import static java.util.Collections.emptyList;
import static java.util.Collections.singletonList;

/**
 * Given a word, computes the scrabble score for that word.
 */
public class Scrabble {
  private final static Map<List<Character>, Integer> POINTS_TABLE = new HashMap<>(7);

  static {
    POINTS_TABLE.put(asList('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'), 1);
    POINTS_TABLE.put(asList('D', 'G'), 2);
    POINTS_TABLE.put(asList('B', 'C', 'M', 'P'), 3);
    POINTS_TABLE.put(asList('F', 'H', 'V', 'W', 'Y'), 4);
    POINTS_TABLE.put(singletonList('K'), 5);
    POINTS_TABLE.put(asList('J', 'X'), 8);
    POINTS_TABLE.put(asList('Q', 'Z'), 10);
  }

  private final int score;

  Scrabble(final String scrabbleInput) {
    if (scrabbleInput == null) {
      score = 0;
      return;
    }
    score = this.computeScore(scrabbleInput.toUpperCase());
  }

  public final int getScore() {
    return this.score;
  }

  private final int computeScore(final String scrabbleInput) {
    return scrabbleInput.chars()
      .mapToObj(ch -> (char) ch)
      .mapToInt(Scrabble::scoreCharacter)
      .sum();
  }

  private static Integer scoreCharacter(final Character ch) {
    final List<Character> foundChSet = POINTS_TABLE.keySet().stream()
      .filter(chList -> chList.contains(ch))
      .findFirst()
      .orElse(emptyList());

    return POINTS_TABLE.getOrDefault(foundChSet, 0);
  }
}
